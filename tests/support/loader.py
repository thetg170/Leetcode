from __future__ import annotations

import bisect
import collections
import heapq
import math
import os
import types
import typing
from pathlib import Path
from typing import Any

from tests.support.nodes import ListNode, Node


def load_module(reference: str | Path, **overrides: Any) -> types.ModuleType:
    """Load a LeetCode submission with the globals normally supplied by the judge."""
    reference_path = Path(reference).resolve()
    target = Path(os.environ.get("KATA_TARGET", reference_path)).resolve()
    if not target.is_file():
        raise FileNotFoundError(f"kata target does not exist: {target}")

    module = types.ModuleType(f"leetcode_{target.parent.name.replace('-', '_')}")
    module.__file__ = str(target)
    module.__dict__.update(
        {
            "List": list,
            "Optional": typing.Optional,
            "ListNode": ListNode,
            "Node": Node,
            "Counter": collections.Counter,
            "defaultdict": collections.defaultdict,
            "deque": collections.deque,
            "bisect": bisect,
            "heapq": heapq,
            "math": math,
            "ceil": math.ceil,
            "floor": math.floor,
        }
    )
    module.__dict__.update(overrides)
    source = target.read_text(encoding="utf-8")
    exec(compile(source, str(target), "exec"), module.__dict__)
    return module


def solution(reference: str | Path, **overrides: Any) -> Any:
    return load_module(reference, **overrides).Solution()

