# Implementation Plan — NeetCode reference solutions

## Summary

Use one upstream Python implementation per problem from a pinned MIT-licensed
NeetCode snapshot, adapted to the local starter interface. Add an optional
metadata field for the archived reference. Keep the draft builder and existing
preview behavior.

## Technical Context

The 107 entries currently use `[files].reference = "starter.py"` to generate
drafts. The other entries use this field for the source of an archived solution.
The workspace asks `lc reference --path` for the active draft's solution and
reads the returned file into a scratch preview. The repository has local helper
types for tree nodes, graph neighbors and random list pointers.

## Constitution Check

Keep starter and review-draft data unchanged. The existing archive remains
readable. Store references locally with provenance, preserve the MIT notice
and validate behavior offline after adding them.

## Project Structure

- `<problem>/reference.py` and optional `[files].archived_solution` metadata.
- `tools/lc.py` — explicit lookup with legacy fallback.
- `practice/neetcode-reference-LICENSE.txt`, `README.md` and the keyboard table.

## Verification

Check all new references for syntax, interface compatibility, importability,
and representative behavior. Use an isolated workspace to verify the preview
with a modified draft. Compare archive and local draft hashes and run the
original pytest suite.
