import math

import pytest

from exception.argument_exception import ArgumentException
from guard import Guard


@pytest.mark.parametrize(
    "param, param_name, message, expected",
    [
        (float('inf'), None, "parameter is an infinity number.", pytest.raises(ArgumentException))
    ]
)
def test_NotInfinityNumber_InfinityNumber_RaisedArgumentException(param, param_name, message, expected):
    with expected as err:
        Guard.not_infinity_number(param=param, param_name=param_name)

    assert message in str(err.value)


@pytest.mark.parametrize(
    "param, param_name, message, expected",
    [
        (14585, None, "parameter is not an infinity number.", pytest.raises(ArgumentException)),
        (5.5, None, "parameter is not an infinity number.", pytest.raises(ArgumentException)),
        (90000000000.0, None, "parameter is not an infinity number.", pytest.raises(ArgumentException))
    ]
)
def test_IsInfinityNumber_NotInfinityNumber_RaisedArgumentException(param, param_name, message, expected):
    with expected as err:
        Guard.is_infinity_number(param=param, param_name=param_name)

    assert message in str(err.value)


def test_NotNAN_NaN_RaisedArgumentException():
    with pytest.raises(ArgumentException) as err:
        Guard.not_nan(param=float("nan"), param_name=None)

    assert "parameter is an NaN." in str(err.value)


def test_NAN_Number_RaisedArgumentException():
    with pytest.raises(ArgumentException) as err:
        Guard.is_nan(param=10, param_name=None)

    assert "parameter is not an NaN." in str(err.value)
