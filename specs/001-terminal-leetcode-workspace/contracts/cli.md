# CLI Contract — lc

`<problem>` accepts a full directory name, a unique slug, or a unique numeric ID. Where optional, it defaults to the active workspace problem. A missing or ambiguous selection produces an actionable diagnostic.

| Command | Behavior |
| --- | --- |
| `lc` | Pick and attach interactively. Use fzf when available and a numbered picker otherwise. |
| `lc pick` | Open a problem from a picker without attaching. Used by the editor popup. |
| `lc resume` | Reattach to the workspace. |
| `lc list` | List discovered problems. |
| `lc search <query>` | Filter problems by the query. |
| `lc open <problem>` | Create or reuse the editor and show the selected problem. |
| `lc next` | Open the next problem. |
| `lc lang en\|vi\|toggle` | Change the statement language without modifying the editor buffer. |
| `lc run [<problem>] [--timeout <seconds>]` | Run a saved Python solution against a supplied JSON sample and show input, expected, and actual. |
| `lc test [<problem>] [--timeout <seconds>]` | Run the curated pytest files against the saved Python solution. |
| `lc status [<problem>]` | Show learning progress. |
| `lc mark <status> [<problem>]` | Record a learner-selected state and practice date. |
| `lc note <text> [<problem>]` | Append a Markdown note to the selected problem. |
| `lc doctor` | Report dependency and workspace setup availability. |
| `lc sync` | Pull the upstream by fast-forward only, with a clean checkout and the workspace editor closed. |

For Run and Test, success exits zero. Wrong answers, runtime errors, timeouts, unavailable cases, and unsupported languages exit nonzero with a diagnostic. The editor shortcuts save the active practice file before invoking Run or Test. Local results never set learning status or LeetCode acceptance.
