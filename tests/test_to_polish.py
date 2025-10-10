from contextlib import nullcontext as does_not_raise

import pytest

from src.parse import parse
from src.to_polish import to_polish


@pytest.mark.parametrize(
        "start, res, expectation",
        [
            (parse("1 + 1"), parse("1 1 +"), does_not_raise()),
            (parse("(2**2 - 1) * (2**10 - 4)**2"), parse("2 2 ** 1 - 2 10 ** 4 - 2 ** *"), does_not_raise()),
            (parse("(10 % 6 // 2) ** 3 + 1"), parse("10 6 % 2 // 3 ** 1 +"), does_not_raise())
        ]
)
def test_to_polish(start, res, expectation):
    with expectation:
        print(start)
        a = to_polish(start)
        assert a == res