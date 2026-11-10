"""Manage two tmux panes without replacing the user's Neovim process."""

from __future__ import annotations

import hashlib
import os
import shutil
import subprocess
import tempfile
import time
from pathlib import Path

PANE_ID = "#{pane_id}"


class Workspace:
    def __init__(self, root: Path) -> None:
        self.root = root.resolve()
        self.name = "lc-" + self._digest(str(self.root))
        self.tmux = ["tmux"]
        socket_name = os.environ.get("LC_TMUX_SOCKET")
        if socket_name:
            self.tmux.extend(["-L", socket_name])
        socket_key = socket_name or os.environ.get("TMUX", "").split(",", 1)[0]
        # TMUX is populated inside a workspace. For default tmux, its path's
        # basename is always "default", which should share the outer CLI state.
        socket_key = Path(socket_key).name if socket_key else "default"
        self.statement = self.root / "practice" / ".lc" / f"statement-{self._digest(socket_key)}.md"

    @staticmethod
    def _digest(value: str) -> str:
        return hashlib.sha256(value.encode()).hexdigest()[:12]

    def _call(self, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
        result = subprocess.run([*self.tmux, *args], capture_output=True, text=True, check=False)
        if check and result.returncode:
            raise RuntimeError(result.stderr.strip() or f"tmux {args[0]} failed")
        return result

    def _get(self, key: str) -> str | None:
        if not shutil.which("tmux"):
            return None
        result = self._call("show-options", "-qv", "-t", f"={self.name}:", key, check=False)
        return result.stdout.strip() or None

    def _set(self, key: str, value: str) -> None:
        self._call("set-option", "-q", "-t", f"={self.name}:", key, value)

    def _pane(self, key: str) -> str | None:
        pane = self._get(key)
        if not pane:
            return None
        panes = self._call(
            "list-panes",
            "-s",
            "-t",
            f"={self.name}",
            "-F",
            "#{pane_id} #{pane_dead}",
            check=False,
        ).stdout.splitlines()
        return pane if f"{pane} 0" in panes else None

    def current(self) -> str | None:
        return self._get("@lc_problem")

    def current_target(self) -> Path | None:
        target = self._get("@lc_target")
        return self.root / target if target else None

    def _set_target(self, directory: str, solution: Path) -> None:
        self._set("@lc_target", str(solution.relative_to(self.root)))
        self._set("@lc_problem", directory)

    def editor_running(self) -> bool:
        return self._pane("@lc_editor") is not None

    def _write_statement(self, content: str) -> None:
        self.statement.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=self.statement.parent,
            delete=False,
        ) as temp:
            temporary = Path(temp.name)
            try:
                temp.write(content)
                temp.close()
                temporary.replace(self.statement)
            finally:
                temporary.unlink(missing_ok=True)

    def _reader(self) -> list[str]:
        return [
            "nvim",
            "--clean",
            "-R",
            "-M",
            "-n",
            "-i",
            "NONE",
            "--cmd",
            "set nomodeline",
            "-c",
            "set wrap linebreak nonumber norelativenumber signcolumn=no",
            "--",
            str(self.statement),
        ]

    def _layout(self, pane: str) -> list[str]:
        columns, rows = self._call(
            "display-message",
            "-p",
            "-t",
            pane,
            "#{pane_width} #{pane_height}",
        ).stdout.split()
        if int(columns) >= 72 or int(rows) < 8:
            return ["-h", "-l", "60%"]
        return ["-v", "-l", "55%"]

    def _split(self, pane: str, command: list[str], *, before: bool = False) -> str:
        layout = self._layout(pane)
        if before:
            layout = [layout[0], "-b", "-l", "40%"]
        return self._call(
            "split-window",
            "-d",
            "-P",
            "-F",
            PANE_ID,
            "-t",
            pane,
            "-c",
            str(self.root),
            *layout,
            *command,
        ).stdout.strip()

    def _rpc(self, socket: str, expression: str) -> str:
        try:
            result = subprocess.run(
                ["nvim", "--headless", "--server", socket, "--remote-expr", expression],
                stdin=subprocess.DEVNULL,
                capture_output=True,
                text=True,
                check=False,
                timeout=2,
            )
        except subprocess.TimeoutExpired:
            raise RuntimeError("Neovim is busy. Finish the current action and try again.") from None
        if result.returncode:
            raise RuntimeError(result.stderr.strip() or "Could not connect to Neovim")
        return result.stdout.strip()

    def _socket(self) -> str:
        socket = self._get("@lc_socket")
        if not socket:
            raise RuntimeError("The workspace has no Neovim server address.")
        return socket

    def _start_editor(self, reader: str, solution: Path) -> None:
        # macOS limits UNIX socket addresses; keep this path short and private.
        runtime = Path(tempfile.mkdtemp(prefix="lc-", dir="/tmp"))
        socket = str(runtime / "nvim")
        try:
            editor = self._split(
                reader,
                [
                    "nvim",
                    "--listen",
                    socket,
                    "-S",
                    str(self.root / "tools" / "lc_nvim.lua"),
                    "--",
                    str(solution),
                ],
            )
        except (OSError, RuntimeError):
            runtime.rmdir()
            raise
        self._set("@lc_socket", socket)
        self._set("@lc_editor", editor)
        self._call("select-pane", "-t", editor)
        deadline = time.monotonic() + 8
        while time.monotonic() < deadline and self.editor_running():
            if Path(socket).exists():
                try:
                    if self._rpc(socket, "luaeval('type(_G.LCOpen)')") == "function":
                        return
                except RuntimeError:
                    pass
            time.sleep(0.1)
        raise RuntimeError(
            f"Neovim did not initialize. Inspect it with tmux attach -t {self.name}."
        )

    def _new_session(self) -> str:
        width, height = shutil.get_terminal_size()
        reader = self._call(
            "new-session",
            "-d",
            "-s",
            self.name,
            "-n",
            "LeetCode",
            "-x",
            str(max(width, 30)),
            "-y",
            str(max(height, 12)),
            "-c",
            str(self.root),
            "-P",
            "-F",
            PANE_ID,
            *self._reader(),
        ).stdout.strip()
        self._set("@lc_reader", reader)
        return reader

    def open(self, directory: str, solution: Path, statement: str) -> None:
        if not shutil.which("nvim"):
            raise RuntimeError("Neovim is required. Run lc doctor.")
        solution = solution.resolve()
        editor = self._pane("@lc_editor")
        if editor:
            # In Vim single-quoted literals a literal apostrophe is doubled.
            path = str(solution).replace("'", "''")
            response = self._rpc(self._socket(), f"luaeval('_G.LCOpen(_A)', '{path}')")
            if response:
                raise RuntimeError(response)
            self._set_target(directory, solution)
            self.refresh(statement)
            self._call("select-pane", "-t", editor)
            return

        reader = self._pane("@lc_reader")
        if reader:
            self.refresh(statement)
        else:
            self._write_statement(statement)
            reader = self._new_session()
        self._start_editor(reader, solution)
        self._set_target(directory, solution)

    def refresh(self, statement: str) -> None:
        reader = self._pane("@lc_reader")
        editor = self._pane("@lc_editor")
        if not reader and not editor:
            return
        self._write_statement(statement)
        if reader:
            self._call(
                "respawn-pane",
                "-k",
                "-t",
                reader,
                "-c",
                str(self.root),
                *self._reader(),
            )
        elif editor:
            self._set("@lc_reader", self._split(editor, self._reader(), before=True))

    def attach(self) -> int:
        command = "switch-client" if os.environ.get("TMUX") else "attach-session"
        return subprocess.run([*self.tmux, command, "-t", f"={self.name}"], check=False).returncode
