# Research

## Map the deck to the local archive

Match the [published NeetCode data](https://github.com/neetcode-gh/leetcode/blob/main/.problemSiteData.json)
by the LeetCode problem slug. The earlier import supplied 150 unique problems
and 43 exact local paths. A numeric-only join would misidentify some older
LeetHub entries, including Binary Search and Koko Eating Bananas.

## Add starter-only entries

Keep original summaries, examples, and Python interfaces with the existing
numbered structure. Separate `starter.py` from archived submissions. This
reuses the established catalog and draft builder. A separate catalog or a live
content downloader would add another way to look up and open a problem.

## Preserve the existing Anki cards

Update only the affected front fields and tags with AnkiConnect. Verify note ID,
card ID, back field, and scheduling values after the change. Creating duplicate
notes would lose the association with the user's study history.
