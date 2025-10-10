import pytest
from contextlib import nullcontext as does_not_raise

from src.parse import parse
from src.errors import CalcError, check_mistakes

@pytest.mark.parametrize(
        "res, expectation",
        [
            (parse("*"), pytest.raises(CalcError)),
            (parse("1 *"), pytest.raises(CalcError)),
            (parse("* 1"), pytest.raises(CalcError)),
            (parse("1 ** 1 1"), pytest.raises(CalcError)),
            (parse("1 * 1 *"), pytest.raises(CalcError)),
            (parse("1-1"), pytest.raises(CalcError)),
            (parse("1+1"), pytest.raises(CalcError)),
            (parse("1/*1"), pytest.raises(CalcError)),
            (parse("1* *1"), pytest.raises(CalcError)),

            (parse("1*1"), does_not_raise()),
            (parse("1**1"), does_not_raise()),
        ]
)
def test_opers_mistakes(res, expectation):
    with expectation:
        check_mistakes(res)
        assert 1 == 1



@pytest.mark.parametrize(
        "res, expectation",
        [
            (parse("((1 + 1)"), pytest.raises(CalcError)),
            (parse("2(*1)"), pytest.raises(CalcError)),
            (parse("(2*)1"), pytest.raises(CalcError)),

            (parse("1 + (1)"), does_not_raise()),
            (parse("1 + (-1)"), does_not_raise()),
            (parse("1 + ((-1))"), does_not_raise()),
            (parse("1 + ((1))"), does_not_raise()),
        ]
)
def test_brackets_mistakes(res, expectation):
    with expectation:
        check_mistakes(res)
        assert 1 == 1