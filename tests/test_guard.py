import pytest

from exception.argument_empty_exception import ArgumentEmptyException
from exception.argument_not_equal import ArgumentNotEqualException
from exception.argument_null_exception import ArgumentNullException
from guard.guard import Guard


class TestGuard:
    @pytest.mark.parametrize(
        "param, param_name, message, expected",
        [
            (None, "test", "test cannot be null", pytest.raises(ArgumentNullException)),
            (None, "test", None, pytest.raises(ArgumentNullException))
        ]
    )
    def test_NotNull_InputParameter_ExpectedResult(self, param, param_name, message, expected):
        with expected:
            Guard.NotNull(param, param_name, message)

    @pytest.mark.parametrize(
        "param, param_name, message, expected",
        [
            (None, "test", "test cannot be empty (should contain at least one element)", pytest.raises(ArgumentEmptyException)),
            ([], "test", "test cannot be empty (should contain at least one element)", pytest.raises(ArgumentEmptyException)),
            (set(), "test", "test cannot be empty (should contain at least one element)", pytest.raises(ArgumentEmptyException)),
            ({}, "test", "test cannot be empty (should contain at least one element)", pytest.raises(ArgumentEmptyException))
        ]
    )
    def test_NotAny_InputParameter_ExpectedResult(self, param, param_name, message, expected):
        with expected:
            Guard.NotAny(param, param_name, message)

    @pytest.mark.parametrize(
        "param, value, message, expected",
        [
            (1, 2, "Equality precondition not met.", pytest.raises(ArgumentNotEqualException)),
            ("xpto", "xpar", "Equality precondition not met.", pytest.raises(ArgumentNotEqualException)),
            (1.0, 2.5, "Equality precondition not met.", pytest.raises(ArgumentNotEqualException)),
        ]
    )
    def test_NotEqualTo_InputParameter_ExpectedResult(self, param, value, message, expected):
        with expected:
            Guard.NotEqualTo(param, value, message)
