from pathlib import Path

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0017-letter-combinations-of-a-phone-number.py"


def test_empty_and_unequal_key_sizes() -> None:
    solver = solution(REFERENCE)
    assert solver.letterCombinations("") == []
    assert sorted(solver.letterCombinations("27")) == [
        "ap",
        "aq",
        "ar",
        "as",
        "bp",
        "bq",
        "br",
        "bs",
        "cp",
        "cq",
        "cr",
        "cs",
    ]
