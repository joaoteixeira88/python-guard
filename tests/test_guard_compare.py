import pytest

from exception.argument_not_equal_exception import ArgumentNotEqualException
from exception.no_such_element_exception import NoSuchElementException
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
        Guard.not_equal_to(param=param, value=value, message=message)


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
    Guard.not_equal_to(param=param, value=value)


@pytest.mark.parametrize(
    "param, value, message, expected",
    [
        ([1, 3, 5], 2, "Collection does not contain the 2", pytest.raises(NoSuchElementException)),
        ("a new test", "xxxx", "Collection does not contain the xxxx", pytest.raises(NoSuchElementException)),
        ({'a': 2}, "b", "Collection does not contain the b", pytest.raises(NoSuchElementException)),
    ]
)
def test_NotIn_MissingValues_RaisedNoSuchElementException(param, value, message, expected):
    with expected as err:
        Guard.not_in(param=param, value=value)

    assert message in str(err.value)
