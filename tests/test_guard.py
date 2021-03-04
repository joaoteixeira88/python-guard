import pytest

from exception.argument_null_exception import ArgumentNullException
from guard.not_null import Guard


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
