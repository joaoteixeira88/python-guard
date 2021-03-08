import pytest

from exception.argument_not_equal_exception import ArgumentNotEqualException
from guard import Guard

@pytest.mark.parametrize(
    "param, value, message, expected",
    [
        (1, 2, "Equality precondition not met.", pytest.raises(ArgumentNotEqualException)),
        ("xpto", "xpar", "Equality precondition not met.", pytest.raises(ArgumentNotEqualException)),
        (1.0, 2.5, "Equality precondition not met.", pytest.raises(ArgumentNotEqualException)),
        ([2], [3], "Equality precondition not met.", pytest.raises(ArgumentNotEqualException)),
        ({'a': 2}, {'a': 3}, "Equality precondition not met.", pytest.raises(ArgumentNotEqualException))
    ]
)
def test_NotEqualTo_NotEqualParameter_RaisedArgumentNotEqualException(param, value, message, expected):
    with expected:
        Guard.NotEqualTo(param, value, message)


@pytest.mark.parametrize(
    "param, value",
    [
        (1, 1),
        ("xpto", "xpto"),
        (1.0, 1.0),
        ([2], [2]),
        ({'a': 2}, {'a': 2}),
    ]
)
def test_NotEqualTo_IqualParameter_ExpectedResult(param, value):
    Guard.NotEqualTo(param, value)