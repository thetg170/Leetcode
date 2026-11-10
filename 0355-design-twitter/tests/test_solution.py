from pathlib import Path

from tests.support.loader import load_module

REFERENCE = Path(__file__).parents[1] / "reference.py"


def test_follow_and_unfollow_change_the_feed() -> None:
    twitter = load_module(REFERENCE).Twitter()
    twitter.postTweet(1, 5)
    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    assert twitter.getNewsFeed(1) == [6, 5]
    twitter.unfollow(1, 2)
    assert twitter.getNewsFeed(1) == [5]


def test_feed_has_at_most_ten_recent_tweets() -> None:
    twitter = load_module(REFERENCE).Twitter()
    twitter.follow(1, 2)
    for tweet in range(1, 13):
        twitter.postTweet(1 + tweet % 2, tweet)
    assert twitter.getNewsFeed(1) == list(range(12, 2, -1))
    assert twitter.getNewsFeed(3) == []
