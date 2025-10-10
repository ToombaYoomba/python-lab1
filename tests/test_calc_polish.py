from contextlib import nullcontext as does_not_raise

import pytest

from src.parse import parse
from src.calc_polish import calc_polish


@pytest.mark.parametrize(
        "start, res, expectation",
        [
            (parse("1 1 +"), float(2), does_not_raise()),
            (parse("2 2 ** 1 - 2 10 ** 4 - 2 ** *"), float(3121200), does_not_raise()),
            (parse("10 6 % 2 // 3 ** 1 +"), float(9), does_not_raise())
        ]
)
def test_to_polish(start, res, expectation):
    with expectation:
        a = calc_polish(start)
        assert a == res