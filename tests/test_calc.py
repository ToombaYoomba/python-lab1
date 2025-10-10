from contextlib import nullcontext as does_not_raise

import pytest

from src.calc import calc
from src.errors import CalcError


@pytest.mark.parametrize(
    "a, b, op, res, expectation",
    [
        (("NUM", float(1)), ("NUM", float(1)), ("-", None), ("NUM", float(0)),does_not_raise()),
        (("NUM", float(1)), ("NUM", float(2)), ("*", None), ("NUM", float(2)),does_not_raise()),
        (("NUM", float(2)), ("NUM", float(3)), ("**", None), ("NUM", float(8)), does_not_raise()),
        (("NUM", float(2)), ("NUM", float(1)), ("/", None), ("NUM", float(2)), does_not_raise()),
        (("NUM", float(3)), ("NUM", float(2)), ("/", None), ("NUM", float(3 / 2)), does_not_raise()),
        (("NUM", float(3.5)), ("NUM", float(2)), ("/", None), ("NUM", float(3.5 / 2)), does_not_raise(),),
        (("NUM", float(3)), ("NUM", float(2)), ("//", None), ("NUM", float(3 // 2)), does_not_raise()),
        (("NUM", float(3)), ("NUM", float(2)), ("%", None), ("NUM", float(3 % 2)), does_not_raise()),
        
        (("NUM", float(1)), ("NUM", float(1)), ("=", None), None, pytest.raises(CalcError)),
        (("NUM", float(3.2)), ("NUM", float(2)), ("//", None), None,pytest.raises(CalcError)),
        (("NUM", float(3)), ("NUM", float(2.2)), ("//", None), None,pytest.raises(CalcError)),
        (("NUM", float(3.2)), ("NUM", float(2.2)), ("//", None), None, pytest.raises(CalcError)),
        (("NUM", float(3.2)), ("NUM", float(2)), ("%", None), None, pytest.raises(CalcError)),
        (("NUM", float(3)), ("NUM", float(2.2)), ("%", None), None, pytest.raises(CalcError)),
        (("NUM", float(3.2)), ("NUM", float(2.2)), ("%", None), None, pytest.raises(CalcError)),
        (("NUM", float(3)), ("NUM", float(0)), ("/", None), None, pytest.raises(CalcError)),
        (("NUM", float(3)), ("NUM", float(0)), ("//", None), None, pytest.raises(CalcError)),
        (("NUM", float(3)), ("NUM", float(0)), ("%", None), None, pytest.raises(CalcError)),
    ],
)
def test_calc(a, b, op, res, expectation):
    with expectation:
        ans = calc(a, b, op)
        assert ans == res


@pytest.mark.parametrize(
    "a, b, op, expectation",
    [
        (("NUM", float(1)), ("NUM", float(1)), ("=", None), pytest.raises(CalcError)),
        (("NUM", float(3.2)), ("NUM", float(2)), ("//", None), pytest.raises(CalcError)),
        (("NUM", float(3)), ("NUM", float(2.2)), ("//", None), pytest.raises(CalcError)),
        (("NUM", float(3.2)), ("NUM", float(2.2)), ("//", None), pytest.raises(CalcError)),
        (("NUM", float(3.2)), ("NUM", float(2)), ("%", None), pytest.raises(CalcError)),
        (("NUM", float(3)), ("NUM", float(2.2)), ("%", None), pytest.raises(CalcError)),
        (("NUM", float(3.2)), ("NUM", float(2.2)), ("%", None), pytest.raises(CalcError)),
        (("NUM", float(3)), ("NUM", float(0)), ("/", None), pytest.raises(CalcError)),
        (("NUM", float(3)), ("NUM", float(0)), ("//", None), pytest.raises(CalcError)),
        (("NUM", float(3)), ("NUM", float(0)), ("%", None), pytest.raises(CalcError)),
    ],
)
def test_calc_errors(a, b, op, expectation):
    with expectation:
        calc(a, b, op)
        assert 1 == 1
