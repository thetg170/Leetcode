"""Python starter for local practice."""

from __future__ import annotations

from tests.support.nodes import TreeNode


class Codec:
    def serialize(self, root: TreeNode | None) -> str:
        raise NotImplementedError

    def deserialize(self, data: str) -> TreeNode | None:
        raise NotImplementedError
