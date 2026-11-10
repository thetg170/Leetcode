# Local testing contract

`Space l t` saves the current Neovim practice buffer and runs its curated local
suite. `lc test <problem>` tests a saved regular workspace solution and
`lc test` uses the active workspace target. Results are local. A blank starter
is expected to fail its suite. The runner retains its current time limit.
