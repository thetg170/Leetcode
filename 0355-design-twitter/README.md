Store posts and follow relationships. A feed contains up to ten of the newest posts written by the requesting user or their current followees, most recent first. Tweet IDs are unique. Following and unfollowing take effect on the next feed request.

## Example

```text
postTweet(1, 11), postTweet(2, 22), follow(1, 2), getNewsFeed(1) → [22,11]
```
