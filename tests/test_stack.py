from contextlib import nullcontext as does_not_raise

import pytest

from src.parse import parse
from src.stack import is_empty, peek, pop, push


#push
@pytest.mark.parametrize(
        "start_st, add_st, res, expectation",
        [
            (parse("1 + 1"), ("NUM", 1.0), parse("1 + 1") + [("NUM", 1.0)], does_not_raise()),
        ]
)
def test_push(start_st, add_st, res, expectation):
    with expectation:
        push(start_st, add_st)
        assert start_st == res


#pop tests
@pytest.mark.parametrize(
        "start_st, res, res_st, expectation",
        [
            (parse("1 + 1"), parse("1 + 1")[-1], parse("1 + 1")[:-1], does_not_raise()),
            ([], None, None, pytest.raises(IndexError))
        ]
)
def test_pop(start_st, res, res_st, expectation):
    with expectation:
        a = pop(start_st)
        assert a == res and start_st == res_st



#peek
@pytest.mark.parametrize(
        "start_st, res, expectation",
        [
            (parse("1 + 1"), parse("1 + 1")[-1], does_not_raise()),
            ([], None, pytest.raises(IndexError))
        ]
)
def test_peek(start_st, res, expectation):
    with expectation:
        a = peek(start_st)
        assert a == res




#is_empty
@pytest.mark.parametrize(
        "start_st, res, expectation",
        [
            (parse("1 + 1"), bool(0), does_not_raise()),
            ([], bool(1), does_not_raise())
        ]
)
def test_is_empty(start_st, res, expectation):
    with expectation:
        a = is_empty(start_st)
        assert a == res



