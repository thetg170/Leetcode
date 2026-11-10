from pathlib import Path

from tests.support.loader import load_module

REFERENCE = Path(__file__).parents[1] / "reference.py"


def test_round_trip_preserves_string_boundaries() -> None:
    codec = load_module(REFERENCE).Codec
    values = ["#:", "", "0#", "12#word", "x y"]
    encoded = codec().encode(values)

    assert isinstance(encoded, str)
    assert codec().decode(encoded) == values


def test_empty_list_and_empty_string_are_distinct() -> None:
    codec = load_module(REFERENCE).Codec
    for values in ([], [""], ["", ""]):
        assert codec().decode(codec().encode(values)) == values
