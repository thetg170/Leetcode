Store multiple timestamped values for a key. Each set call arrives with a timestamp greater than the previous set call. A get call retrieves the value at the latest stored time for that key not exceeding the requested time. Return an empty string when there is no match.

## Example

```text
set('k', 'old', 2), set('k', 'new', 5), get('k', 4) → 'old'
```
