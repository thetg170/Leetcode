"""Python starter for local practice."""

from __future__ import annotations


class Twitter:
    def __init__(self) -> None:
        raise NotImplementedError

    def postTweet(self, userId: int, tweetId: int) -> None:
        raise NotImplementedError

    def getNewsFeed(self, userId: int) -> list[int]:
        raise NotImplementedError

    def follow(self, followerId: int, followeeId: int) -> None:
        raise NotImplementedError

    def unfollow(self, followerId: int, followeeId: int) -> None:
        raise NotImplementedError
