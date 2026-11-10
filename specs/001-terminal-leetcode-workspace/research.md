# Research — Terminal LeetCode Workspace

## One tmux session per checkout

**Decision.** Use one tmux session keyed by the resolved checkout path. Give the statement and editor separate panes. Detach and reattach to the same editor, refresh the statement independently, and use existing tmux pane navigation, zoom, and resize.

**Rationale.** tmux 3.6a supports detached creation, explicit pane targets, and a picker popup. Pane IDs stay usable when indexes change. Two checkouts can run separately even when their directory names match.

**Alternatives considered.** A single Neovim split would tie statement rendering to the editor layout. Recreating both panes on each problem switch would discard unsaved buffers.

## Neovim editor and local statements

**Decision.** Keep the installed Neovim configuration for the editor. Load workspace mappings only inside its pane. Use a private Unix socket and `:hide edit` for problem switches, and show a generated Markdown statement in a separate read-only pane. Put the socket under a short temporary path for macOS.

**Rationale.** The installed Neovim 0.12.1 help documents `:hide edit` as preserving changes in a hidden buffer. `--remote-expr` addresses the existing editor directly without typing into the active mode. A separate viewer allows language changes while the editor remains in insert mode.

**Alternatives considered.** Sending raw keystrokes is sensitive to editor mode. A third-party viewer or translation service would add setup or network requirements.

## Reuse the kata fixtures

**Decision.** Read existing metadata and statements, derive a Python practice stub with the existing tooling, and run curated pytest files with `KATA_TARGET` set to the separate practice solution. Use an explicit JSON example for `lc run`. Apply a timeout to each run. Provide read/edit support for SQL.

**Rationale.** The repository has 30 curated Python test files and no shared SQL test schema. The kata fixtures already handle LeetCode-style Python submissions and their expected data structures. A JSON case provides readable inputs and outputs for the Two Sum sample.

**Alternatives considered.** A new test harness for all archived problems would duplicate fixture logic. Implicitly running archived submissions would not verify the current practice file.

## Portability and synchronization

**Decision.** Bootstrap from the checkout via uv and link the launcher into a per-user bin directory. Version practice data by problem. Require a closed workspace editor and a clean checkout before `git pull --ff-only --no-rebase --no-autostash`. Keep reviewing, staging, committing, and pushing manual.

**Rationale.** A checkout at a different path can use the same relative data layout. Git 2.50.1 supports the explicit fast-forward and no-autostash flags. Checking for in-progress Git operations covers states that can appear clean after conflict resolution. Keeping the editor closed protects unsaved work during sync.

**Alternatives considered.** Auto-stash can introduce a conflict when reapplying changes. A database or automatic remote writes would make progress harder to review with Git.
