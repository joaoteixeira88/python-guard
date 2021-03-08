import pytest

from exception.argument_exception import ArgumentException
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
        Guard.EmailNotValid(param=param, param_name=param_name)

    assert message in str(err.value)
