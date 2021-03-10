import pytest

from exception.argument_exception import ArgumentException
from exception.argument_out_of_range_exception import ArgumentOutOfRangeException
from guard import Guard


@pytest.mark.parametrize(
    "param, param_name, message, expected",
    [
        ("x.pt", None, "parameter is not a valid email.", pytest.raises(ArgumentException)),
        ("xxx@aa", None, "parameter is not a valid email.", pytest.raises(ArgumentException)),
        ("@", None, "parameter is not a valid email.", pytest.raises(ArgumentException)),
        ("xxxxx", None, "parameter is not a valid email.", pytest.raises(ArgumentException))
    ]
)
def test_EmailNotValid_InvalidEmail_RaisedArgumentException(param, param_name, message, expected):
    with expected as err:
        Guard.email_not_valid(param=param, param_name=param_name)

    assert message in str(err.value)


def test_LengthNotGreaterThan_InvalidLength_RaisedArgumentOutOfRangeException():
    with pytest.raises(ArgumentOutOfRangeException) as err:
        Guard.length_not_greater_than(param=[1, 2, 3, 4], threshold=2, param_name=None)

    assert "parameter length cannot be greater than 2." in str(err.value)


def test_LengthNotLessThan_InvalidLength_RaisedArgumentOutOfRangeException():
    with pytest.raises(ArgumentOutOfRangeException) as err:
        Guard.length_not_less_than(param=[1, 2, 3, 4], threshold=10, param_name=None)

    assert "parameter length cannot be less than 10." in str(err.value)


def test_IsNotWhiteSpace_StringWithLetters_RaisedArgumentException():
    with pytest.raises(ArgumentException) as err:
        Guard.is_not_white_space(param="      ", param_name=None)

    assert "parameter is not a whitespace." in str(err.value)
