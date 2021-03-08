import pytest

from exception.argument_not_instance_of_exception import ArgumentNotInstanceOfException
from guard import Guard


@pytest.mark.parametrize(
    "param, typeof, param_name, message, expected",
    [
        (2, str, None, "parameter is not from type <class 'str'>.", pytest.raises(ArgumentNotInstanceOfException)),
        ([], dict, None, "parameter is not from type <class 'dict'>.", pytest.raises(ArgumentNotInstanceOfException)),
        ("test", bool, None, "parameter is not from type <class 'bool'>.", pytest.raises(ArgumentNotInstanceOfException))
    ]
)
def test_IsNotInstanceOfType_InvalidType_RaisedArgumentNotInstanceOfException(param, typeof, param_name,
                                                                              message, expected):
    with expected as err:
        Guard.IsNotInstanceOfType(param=param, typeof=typeof, param_name=param_name)

    assert message in str(err.value)