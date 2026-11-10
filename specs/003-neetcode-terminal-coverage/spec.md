# Feature Specification — Complete NeetCode 150 terminal coverage

**Feature Directory** `specs/003-neetcode-terminal-coverage`  
**Created** 2026-11-10  
**Status** Implemented

## User Scenarios & Testing

### US1 — Open any card in the terminal (P1)

Copy the command from any of the 150 Anki cards and run it from any directory.
The existing tmux workspace displays the named problem and opens a fresh
Python attempt in Neovim. The 107 newly covered problems have offline EN/VI
summaries, a small example and a method or design-class skeleton.

**Independent test** Verify that all 150 card commands resolve uniquely and
launch a draft in an isolated tmux workspace. For a newly added class-based
problem and a data-structure problem, verify that the skeleton has the expected
interface and can load in the project environment.

### US2 — Preserve the archive and cards (P1)

The 43 existing problem paths, archived solutions and drafts remain in place.
The 107 existing Anki notes that had web links gain a command in their front
field and remain the same cards with the same back and study state.

**Independent test** Verify archive file hashes, unchanged Git HEAD and index,
and preservation of all 150 note IDs, card IDs, and answer text.

## Functional Requirements

- **FR-001** Match the 150 cards against the NeetCode list already used to create
  the deck. Reuse the repository's existing paths where they differ from the
  published problem identifiers.
- **FR-002** Add exactly 107 new Python practice entries with original EN and VI
  summaries, a worked input/output example, a source link, and starter signatures.
- **FR-003** Reuse the current `lc review` entry point and its ignored local draft
  storage. Existing local test behavior remains available where cases exist.
- **FR-004** Add verified review commands to the 107 Anki card fronts, preserving
  the online links and answers. Replace the web-only tag with a missing-test tag.
- **FR-005** Preserve existing solutions, dotfiles, and Git history. Anki remains
  responsible for the review schedule.

## Success Criteria

- All 150 Anki commands open the corresponding local Python practice problem.
- All new starters can be loaded and create unimplemented drafts with their
  expected method signatures.
- The 107 cards retain their note and card identities, and local test availability
  is communicated accurately.
