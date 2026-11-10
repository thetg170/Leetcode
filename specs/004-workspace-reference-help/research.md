# Research

## Resolve by the active buffer

Review drafts live under ignored machine-local directories. Deriving the
problem from a filename or the last tmux selector could show the wrong reference
for an older buffer. Reuse the same target resolver as Run/Test.

## Display in a scratch view

Populate a floating scratch buffer from the reference and make it read-only.
This separates display from both the archive file and the active draft. A
dedicated Lua script can register the new mappings in an already-running editor
without recreating the workspace.

## Keep one keyboard reference

Load one local Markdown table in the help view and link it in README. Document
the distinction between detaching the tmux client and quitting both panes.
