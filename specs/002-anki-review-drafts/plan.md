# Implementation Plan — Practice from an Anki card

## Summary

Add `lc review <problem>` to the existing CLI. Reuse the tmux session, Python
signature builder, Neovim actions and runner. Keep fresh attempts in machine-local
storage and keep all scheduling in Anki.

## Technical Context

Existing Python 3.12, tmux and Neovim integration. `lc` is already linked on
PATH. Existing suite has 33 tests. The Python runner accepts an explicit target
and the workspace keymaps pass the active buffer path. No new dependencies.

## Constitution Check

Create drafts under ignored `practice/.lc/`, separate from the shareable
solution and legacy kata data. Preserve modified buffers when switching. Use
explicit test targets and the existing timeout policy. Provide a plain shell
command that works from either clone.

## Project Structure

- `tools/lc.py` — review command, draft creation, statement mode and runner target validation.
- `tools/lc_workspace.py` — remember the selected file in the current tmux session.
- `README.md` — Anki card and local draft workflow in Vietnamese.

## Verification

Use a disposable checkout and isolated tmux. Validate fresh attempts, saved and
unsaved buffers, test target selection, language, resume and Git ignore rules.
Run the original pytest suite, lint and type checks. Compare existing solution
and dotfiles hashes.
