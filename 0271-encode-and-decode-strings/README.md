Design a codec that packs a list of strings into one string and reconstructs the original list exactly, in order. The list and its individual strings can be empty, and the strings may contain separator characters.

## Example

```text
decode(encode(['a#b', '', 'xy'])) → ['a#b', '', 'xy']
```
