#!/bin/sh
set -eu

case "${1:-}" in
    ""|--offline) ;;
    *) echo 'Usage: tools/bootstrap-lc.sh [--offline]' >&2; exit 2 ;;
esac
for tool in uv tmux nvim git; do
    command -v "$tool" >/dev/null || { echo "Missing: $tool" >&2; exit 1; }
done
root=$(CDPATH='' cd -- "$(dirname "$0")/.." && pwd -P)
launcher=$root/bin/lc
bin_dir=${LC_BIN_DIR:-"$HOME/.local/bin"}
link=$bin_dir/lc
if [ -e "$link" ] || [ -L "$link" ]; then
    if [ "$(readlink "$link" || true)" != "$launcher" ]; then
        echo "Already exists: $link. Use $launcher or choose LC_BIN_DIR." >&2
        exit 1
    fi
fi
# The optional argument is either absent or exactly --offline.
UV_PROJECT_ENVIRONMENT="$root/.venv" uv sync --project "$root" --locked --dev "$@"
mkdir -p "$bin_dir"
if [ ! -L "$link" ]; then
    ln -s "$launcher" "$link"
fi
printf 'Installed %s. Add %s to PATH if needed.\n' "$link" "$bin_dir"
"$link" doctor
