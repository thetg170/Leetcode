# Research

## Reuse local contracts

The current catalog reports 150 NeetCode entries and 20 curated test files.
The runner already executes one configured pytest file and sets the saved draft
path as `KATA_TARGET`. Test files can use the existing support loader with the
appropriate reference when run directly.

## Validate semantics

Use original examples and focused additional cases. Compare unordered output
without silently discarding duplicates, check valid topological and ordering
constraints, and inspect mutated arguments or object identity as needed.
Stateful designs are checked as operation sequences.

## Isolate verification

Write and run tests in a disposable copy first. It allows replacing a test draft
with a correct, wrong or incomplete implementation while keeping the user's
actual attempts and archived solutions intact.
