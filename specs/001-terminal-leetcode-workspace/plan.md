# Implementation Plan — Terminal LeetCode Workspace

## Summary

Layer a Python CLI over the existing archive. Use tmux for the layout and a workspace-local Lua module for Neovim actions. Keep the editor alive via its local control socket and refresh the reader independently.

## Technical Context

- 495 numbered directories. Git tracks 265 Python and 225 SQL files, including LeetHub imports with HTML in README.md.
- 265 existing Python metadata files and 30 curated test files. The baseline suite has 33 passing tests. LeetHub history shows prior submissions, while local study progress is separate.
- The working tree already contains 332 changes, including local kata tooling and metadata. A second clone requires intentionally sharing those dependencies with the MVP.
- Dotfiles use symlinks for zsh, tmux and LazyVim. tmux already supports keyboard navigation and resize. Neovim has Markdown rendering, Snacks and kata mappings under `<leader>k`. zsh already puts `~/.local/bin` on PATH. fzf and bat are installed. No dotfiles edits are needed.
- Reuse uv, Python 3.12+, pytest, the kata statement parser, signature generation and `KATA_TARGET`. SQL can be opened and edited, with no local judge schema assumed.

## Constitution Check

Archive and dotfiles remain in place. New work happens in `solution.py` or `solution.sql`. Prefer original VI/EN study summaries over publishing copied statements. Use explicit, clean fast-forward pull and manual reviewed push.

## Project Structure

- `bin/lc`, `tools/bootstrap-lc.sh` — portable entry point and setup.
- `tools/lc.py`, `tools/lc_workspace.py`, `tools/lc_nvim.lua` — catalog, tmux integration and editor commands.
- `tools/lc_runner.py`, `tools/lc_pytest.py` — local examples, pytest and result reporting.
- `practice/statements/<directory>/<lang>.md` — optional local or shareable original summaries.
- `practice/examples/<directory>.json` — optional JSON cases with a method, arguments and expected result.
- `practice/progress/<directory>.json` — explicit study state and date. Existing `notes.md` remains usable.
- `practice/.lc/` — ignored machine-local workspace state. Socket endpoints use a private temporary directory.

## Verification

Use an isolated tmux server and disposable checkout with a space in its path. Exercise unsaved buffers, language fallback, Git conflict/dirty/diverged cases, bootstrap and local runner outcomes. Keep all existing pytest tests passing.
