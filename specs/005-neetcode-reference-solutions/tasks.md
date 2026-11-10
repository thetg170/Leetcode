# Tasks — NeetCode reference solutions

## Phase 1 — Setup

- [x] T001 Identify the 107 starter entries and resolve the Spec Kit templates in `specs/005-neetcode-reference-solutions/`.

## Phase 2 — Foundation

- [x] T002 Separate archived solution lookup from draft generation in `tools/lc.py`.

## Phase 3 — US1: Read a local reference

- [x] T003 [US1] Adapt one Python implementation per starter-based problem into `<problem>/reference.py` and point each `meta.toml` to it.
- [x] T004 [US1] Preserve MIT provenance in `practice/neetcode-reference-LICENSE.txt` and update the README and keyboard table.

## Phase 4 — US2: Preserve practice behavior

- [x] T005 [US2] Verify starter, archive, draft and Git preservation. Check reference code, existing tests and the actual preview. Record evidence here.

## Dependencies and execution

T001 → T002 → T003 → T005. Complete attribution and help in T004 once the
source and layout are pinned. Validate staged source files before making them
visible in the workspace.

## Verification — 2026-11-10

- All 107 reference files matched the starter class and method signatures.
  Each reference passed its checked-in statement example. Additional checks
  passed for 34 structure and graph problems and 1,560 deterministic cases
  across 13 algorithms. Large grids and skewed codec trees passed separately.
- The CLI returned readable paths for all 150 entries. It used the new file
  for 107 entries and the existing archive path for the other 43.
- Used the actual `Space l s` mapping for Invert Binary Tree, Clone Graph and
  Time Based Key Value Store in isolated tmux. In all three, the preview
  matched the reference file and was read-only. Closing it restored the same
  window, cursor and modified draft. Fresh attempts still contained the
  unimplemented starter.
- Verified the hashes of 1,633 pre-existing problem files. The only changes
  to those files were the intended metadata field additions. The license
  matches the pinned upstream copy. The 33 existing tests, Ruff checks and
  `git diff --check` passed. Git HEAD and index matched their baselines.
