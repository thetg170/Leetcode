# Feature Specification — NeetCode reference solutions

**Feature Directory** `specs/005-neetcode-reference-solutions`  
**Created** 2026-11-10  
**Status** Implemented

## User Scenarios & Testing

### US1 — Read a solution in the workspace (P1)

Open any of the 107 starter-based problems and press `Space l s`. The editor
shows a working Python reference offline. Close the read-only view and return
to the same draft and cursor.

**Independent test** Open references for a tree, graph, and design-class
problem. Compare the preview with the configured file. Use the existing
reference command to verify all 107 paths.

### US2 — Continue solving from a blank draft (P1)

A new `lc review` attempt still loads the starter signature. Existing archived
solutions and draft files stay intact. Source and license are available with
the imported reference files.

**Independent test** Compare starter, archive and draft hashes. Start a fresh
attempt and inspect its unimplemented method. Run behavioral checks on the
references separately from user-facing draft tests.

## Functional Requirements

- **FR-001** Provide one executable Python reference per starter-based entry,
  with a compatible class and public methods.
- **FR-002** Keep each new reference separate from its starter, saved solution
  and local attempts. Resolve it via optional metadata. Preserve legacy
  lookup and the missing-reference diagnostic.
- **FR-003** Reuse the existing workspace keymap and read-only preview.
- **FR-004** Preserve applicable source attribution and license. Keep the
  references available offline and avoid new dependencies.
- **FR-005** Preserve the pre-existing archive and draft bytes. No commit or
  push as part of the implementation.

## Success Criteria

- All 107 entries return readable reference paths. The existing 43 entries
  retain their previous lookup behavior.
- New reference files load and run through their starter interfaces on the
  specified validation cases.
- Existing archive, starter and draft content is unchanged.
