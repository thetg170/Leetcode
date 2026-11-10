# Tasks — Practice from an Anki card

## Phase 1 — Setup

- [x] T001 Resolve the Spec Kit templates and record the approved scope and contracts under `specs/002-anki-review-drafts/`.

## Phase 2 — Foundation

- [x] T002 Record the active checkout-relative file in `tools/lc_workspace.py`, with fallback for older sessions.

## Phase 3 — US1: Start from a card

- [x] T003 [US1] Add `lc review`, fresh ignored Python drafts, and the review banner in `tools/lc.py`.
- [x] T004 [US1] Document the Anki card and repeat workflow in `README.md`.

## Phase 4 — US2: Keep workspace and test state consistent

- [x] T005 [US2] Route active and explicit Run/Test, language changes and resume in `tools/lc.py`.

## Phase 5 — Verification

- [x] T006 Check both stories in isolated tmux, validate the old suite, and record evidence in `specs/002-anki-review-drafts/tasks.md`.

## Dependencies and execution

T001 → T002 → T003 → T005 → T006. T004 can be written alongside the code
once the command contract is settled. Start with the card-to-draft scenario,
then verify switching and compatibility.

## Verification — 2026-11-10

- **FR-001** The Two Sum card command attached to real tmux from outside a checkout with a space in its path. The Python draft contained the method signature and an unimplemented body.
- **FR-002** Two attempts had different ignored paths. The first attempt retained unsaved changes after switching to the second. The existing Two Sum solution, kata scratch and LeetHub submission retained their hashes.
- **FR-003** EN/VI and the review banner shared the same attempt. Verified Run and Test on the active draft, Test via the actual Neovim mapping, explicit selector against the separate main solution, resume after quitting the editor, and legacy fallback without the target option.
- **FR-004** Documented the plain card command and manual Anki grading. The CLI and test workflow ran using the existing environment and local data.
- **FR-005** Verified the Python-only diagnostic for SQL, missing-test diagnostic and normal `lc open` behavior.
- Original pytest suite passed 33/33. Ruff, basedpyright and `git diff --check` passed.
