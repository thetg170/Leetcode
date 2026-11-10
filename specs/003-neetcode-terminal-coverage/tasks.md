# Tasks — Complete NeetCode 150 terminal coverage

## Phase 1 — Setup

- [x] T001 Resolve Spec Kit templates and map the 150 entries against the existing catalog in `specs/003-neetcode-terminal-coverage/`.

## Phase 2 — Foundation

- [x] T002 Extend the shared draft node imports in `tools/kata.py` and node shapes in `tests/support/nodes.py`.

## Phase 3 — US1: Local practice

- [x] T003 [US1] Add 107 original EN/VI summaries, starter interfaces, and metadata in the numbered directories and `practice/statements/`.
- [x] T004 [US1] Verify all 150 review commands in an isolated workspace and document the workflow in `README.md`.

## Phase 4 — US2: Preserve and update existing cards

- [x] T005 [US2] Update the 107 Anki card fronts and tags through AnkiConnect and verify all card identities, answers and schedule values.
- [x] T006 [US2] Verify archive integrity, legacy tests and unchanged Git state. Record results in `specs/003-neetcode-terminal-coverage/tasks.md`.

## Dependencies and execution

T001 → T002 and T003 → T004 → T005 → T006. Drafts and Anki notes are verified
independently. Validate the local paths before changing the commands in Anki.

## Verification — 2026-11-10

- The 150 exact paths were unique and resolved to Python entries. All 107 new
  entries rendered original EN and VI statements with examples and contained
  an unimplemented starter. Ruff and basedpyright passed for new starters and
  shared node classes.
- All 150 `lc review` commands opened and loaded a draft in the same isolated
  tmux session and Neovim process. Batch verification used a separate Neovim
  profile after bursts of opens triggered busy responses from the editor with
  its usual plugins. Separately, Clone Graph opened in a real attached terminal
  with the usual configuration and then switched to Time Based Key Value Store.
- The Vietnamese pane, English pane, and missing-test behavior were verified
  on the new Invert Binary Tree entry. The 20 existing curated suites remain.
  The original pytest suite passed 33/33.
- AnkiConnect updated 107 existing note fronts. Verified all 150 unique
  commands, note IDs, card IDs, back fields and scheduling values. The 107
  affected cards have `needs-local-tests` in place of `web-only`.
- All 1,312 pre-existing archive files retained their hashes. Dotfiles, Git
  HEAD, and the staged diff matched their baselines. `git diff --check` passed.
