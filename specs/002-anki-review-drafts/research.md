# Research

## Connect Anki to the workspace

Use a copyable command on the front of a card. It resolves a repository selector
on either Mac. An add-on or local URL handler would require separate setup on
each machine and is unnecessary for this workflow.

## Store independent attempts

Use a unique subdirectory under the existing ignored workspace directory for
each attempt. Keep the basename `solution.py` so the existing Neovim keymaps
work even in an already-running editor. Reuse the signature generator. A single
overwritten scratch path could discard a previous attempt or collide with a
modified buffer.

## Select the test target

A Neovim keymap already passes the current buffer path, and the test runner
accepts a target. Validate the path and derive its problem. In a shell, the
argument-free command uses the active workspace file and an explicit selector
uses the regular solution.
