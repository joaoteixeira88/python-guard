import pytest

from exception.argument_not_null_exception import ArgumentNotNullException
from exception.argument_null_exception import ArgumentNullException
from guard import Guard


@pytest.mark.parametrize(
    "param, param_name, message, expected",
    [
        (None, "test", "test cannot be null", pytest.raises(ArgumentNullException)),
        (None, "test", None, pytest.raises(ArgumentNullException))
    ]
)
def test_NotNull_InputParameter_ExpectedResult(param, param_name, message, expected):
    with expected:
        Guard.not_null(param, param_name, message)


@pytest.mark.parametrize(
    "param, param_name, message, expected",
    [
        (1, "test", "test cannot be null", pytest.raises(ArgumentNotNullException)),
        ([], "test", None, pytest.raises(ArgumentNotNullException))
    ]
)
def test_Null_InputParameter_RaiseArgumentNotNullException(param, param_name, message, expected):
    with expected:
        Guard.null(param, param_name, message)