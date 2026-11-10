# Implementation Plan — Workspace reference and keyboard help

## Summary

Add two normal-mode mappings to the existing Neovim workspace. Use the Python
catalog to find the archived solution for the current buffer. Display code and
keyboard help in read-only editor previews.

## Technical Context

The repo already supplies Python, tmux, a Neovim startup script, and `lc`
workspace target validation for both regular files and review drafts. The
published archive and local review attempts use separate paths. New NeetCode
entries can reference `starter.py`. The current shell uses `Ctrl+Space` as its
tmux prefix.

## Constitution Check

Use local metadata and a scratch buffer. Avoid loading the reference as an
editable file, changing a draft on disk, touching dotfiles, or adding runtime
dependencies. The help text should describe the current controls.

## Project Structure

- `tools/lc.py` — reference lookup using workspace target resolution.
- `tools/lc_nvim_views.lua` and `tools/lc_nvim.lua` — preview and keymaps.
- `practice/workspace-shortcuts.md` and `README.md` — keyboard reference.

## Verification

Use an isolated tmux server and a checkout path with a space. Verify both maps
with modified draft content, a starter-only item, switching while a view is
open, the existing test shortcut, and initial and repeated view registration.
