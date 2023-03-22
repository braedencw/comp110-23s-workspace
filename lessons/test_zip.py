"""Unit Tests for zip function"""

from lessons.zip import zip

def test() -> None:
    test_keys: list[str] = ["Dad", "Mom", "Brother"]
    test_values: list[int] = [60, 48, 14]
    assert zip(test_keys, test_values) == {"Dad": 60, "Mom": 48, "Brother": 14}

