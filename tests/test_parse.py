import pytest
from contextlib import nullcontext as does_not_raise

from src.parse import parse
from src.Errors import CalcError

@pytest.mark.parametrize(
        "res, expectation",
        [
            ("1 + 1", does_not_raise()),
            ("1 + -1", does_not_raise()),
            ("", pytest.raises(CalcError))
        ]
)
def test_parse(res, expectation):
    with expectation:
        e = parse(res)
        assert 1 == 1
        # assert len(parse(res)) == 0