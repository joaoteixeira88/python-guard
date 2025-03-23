import pytest

from exception.argument_empty_exception import ArgumentEmptyException
from exception.argument_exception import ArgumentException
from guard import Guard


@pytest.mark.parametrize(
    "param, param_name, message, expected",
    [
        (None, "test", "test cannot be empty (should contain at least one element)",
         pytest.raises(ArgumentEmptyException)),
        ([], "test", "test cannot be empty (should contain at least one element)",
         pytest.raises(ArgumentEmptyException)),
        (set(), "test", "test cannot be empty (should contain at least one element)",
         pytest.raises(ArgumentEmptyException)),
        ({}, "test", "test cannot be empty (should contain at least one element)",
         pytest.raises(ArgumentEmptyException))
    ]
)
def test_NotAny_InputParameter_ExpectedResult(param, param_name, message, expected):
    with expected:
        Guard.not_any(param=param, param_name=param_name, message=message)


@pytest.mark.parametrize(
    "param, value, param_name, message, expected",
    [
        ([], 2, None, "parameter must have at least 2 elements.", pytest.raises(ArgumentException)),
        ({"a": 1}, 2, None, "parameter must have at least 2 elements.", pytest.raises(ArgumentException)),
        ({1, 2, 3}, 20, None, "parameter must have at least 20 elements.", pytest.raises(ArgumentException))
    ]
)
def test_NotLessThan_LessThanThreshold_RaisedArgumentException(param, value, param_name,
                                                                         message, expected):
    with expected as err:
        Guard.min_count(param=param, threshold=value, param_name=param_name)

    assert message in str(err.value)


@pytest.mark.parametrize(
    "param, message, expected",
    [
        ([1, 2, 3, 1], "The collection have duplicated elements.", pytest.raises(ArgumentException)),
        (["test", "test"], "The collection have duplicated elements.", pytest.raises(ArgumentException))
    ]
)
def test_ContainsDuplicated_DuplicatedElements_RaisedArgumentException(param, message, expected):
    with expected as err:
        Guard.contains_duplicated(param=param)

    assert message in str(err.value)
