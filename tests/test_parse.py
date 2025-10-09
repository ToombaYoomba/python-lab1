from contextlib import nullcontext as does_not_raise

import pytest

from src.Errors import CalcError
from src.parse import parse


@pytest.mark.parametrize(
        "ini, res, expectation",
        [
            ("1 + 1", [("NUM", float(1)), ("+", None), ("NUM", float(1))], does_not_raise()),
            ("1 + -1", [("NUM", float(1)), ("+", None), ("NUM", float(-1))], does_not_raise()),
            ("1 + (-1)", [("NUM", float(1)), ("+", None), ("(", None), ("NUM", float(-1)), (")", None)], does_not_raise())
        ]
)
def test_parse(ini, res, expectation):
    with expectation:
        a = parse(ini)
        assert a == res



@pytest.mark.parametrize(
        "res, expectation",
        [
            ("", pytest.raises(CalcError)),
            ("          ", pytest.raises(CalcError))
        ]
)
def test_0_parse(res, expectation):
    with expectation:
        parse(res)
        assert 1 == 1