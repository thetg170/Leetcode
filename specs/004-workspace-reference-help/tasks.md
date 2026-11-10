# Tasks — Workspace reference and keyboard help

## Phase 1 — Setup

- [x] T001 Resolve Spec Kit templates and define preview, help and draft preservation in `specs/004-workspace-reference-help/`.

## Phase 2 — Foundation

- [x] T002 Add read-only reference lookup to `tools/lc.py` and reuse workspace target validation.

## Phase 3 — US1: Read a reference

- [x] T003 [US1] Add the scratch preview and reference mapping in `tools/lc_nvim_views.lua` and load it from `tools/lc_nvim.lua`.

## Phase 4 — US2: Look up keys

- [x] T004 [US2] Add the shared shortcut table, help mapping and README link in `practice/workspace-shortcuts.md`, `tools/lc_nvim_views.lua` and `README.md`.

## Phase 5 — Verification

- [x] T005 Verify the mappings, unchanged modified drafts, normal switching, missing references and existing test behavior. Record checks in `specs/004-workspace-reference-help/tasks.md`.

## Dependencies and execution

T001 → T002 → T003 → T005. The keyboard table in T004 can be written
independently of the reference lookup. Verify both mappings before updating
an existing attached editor.

## Verification — 2026-11-10

- Used the actual Neovim keymaps in an isolated tmux session and a checkout
  whose path contained spaces. The reference matched the archived file and
  opened in a non-modifiable, read-only scratch buffer.
- After closing each preview, the draft buffer, window, cursor, change tick
  and modified state matched their prior values. Opening and closing the
  reference left the draft and archived reference bytes unchanged.
- The lookup followed an older draft open in the editor even when tmux selected
  a different problem. Opening another problem from the shell dismissed the
  preview and returned to the normal editor. Starter-only Invert Binary Tree
  showed the expected notification.
- Verified repeated mapping registration and ran the existing Test shortcut on
  a solved disposable Two Sum draft. All 33 existing tests passed. Ruff,
  basedpyright and `git diff --check` passed.
- Loaded the shortcuts in the already attached workspace. The same buffer,
  window, cursor and modified state remained active. Git HEAD and the staged
  diff matched the original checkout state.
