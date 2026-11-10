"""Python starter for local practice."""

from __future__ import annotations


class TimeMap:
    def __init__(self) -> None:
        raise NotImplementedError

    def set(self, key: str, value: str, timestamp: int) -> None:
        raise NotImplementedError

    def get(self, key: str, timestamp: int) -> str:
        raise NotImplementedError
