# Reference lookup

`lc reference <problem>` prints the local path. Neovim uses its existing
buffer-specific option and read-only preview. A configured archived solution
takes precedence over the legacy reference. If there is no readable solution,
the existing message points to Anki or the online problem.

`lc review <problem>` still generates a fresh, unimplemented attempt from
`files.reference`.
