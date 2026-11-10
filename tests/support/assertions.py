from __future__ import annotations

from collections.abc import Iterable
from typing import Any


def normalized_nested(values: Iterable[Iterable[Any]]) -> list[tuple[Any, ...]]:
    return sorted(tuple(sorted(group)) for group in values)

