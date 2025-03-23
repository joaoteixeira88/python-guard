import pytest

from exception.argument_out_of_range_exception import ArgumentOutOfRangeException
from guard import Guard


@pytest.mark.parametrize(
    "param, value, param_name, message, expected",
    [
        (2, 1, None, "param cannot be greater than 1.", pytest.raises(ArgumentOutOfRangeException)),
        (
                5.43345, 3.3434, "test", "test cannot be greater than 3.3434.",
                pytest.raises(ArgumentOutOfRangeException)),
    ]
)
def test_NotGreaterThan_GreaterThanThreshsold_RaisedArgumentOutOfRangeException(param, value, param_name,
                                                                                message, expected):
    with expected:
        Guard.not_greater_than(param=param, threshold=value, param_name=param_name, message=message)


@pytest.mark.parametrize(
    "param, value",
    [
        (1, 2),
        (3.43345, 5.3434)
    ]
)
def test_NotGreaterThan_LowerThanThreshold_RaisedArgumentOutOfRangeException(param, value):
    Guard.not_greater_than(param=param, threshold=value)


@pytest.mark.parametrize(
    "param, value, param_name, message, expected",
    [
        (1, 2, None, "parameter cannot be less than 2.", pytest.raises(ArgumentOutOfRangeException)),
        (
                3.43345, 5.3434, "test", "test cannot be less than 5.3434.",
                pytest.raises(ArgumentOutOfRangeException)),
    ]
)
def test_NotLessThan_LessThanThreshold_RaisedArgumentOutOfRangeException(param, value, param_name,
                                                                         message, expected):
    with expected as err:
        Guard.not_less_than(param=param, thershold=value, param_name=param_name)

    assert message in str(err.value)


@pytest.mark.parametrize(
    "param, value",
    [
        (2, 1),
        (5.43345, 3.3434)
    ]
)
def test_NotLessThan_GreaterThanThreshold_RaisedArgumentOutOfRangeException(param, value):
    Guard.not_less_than(param=param, thershold=value)
