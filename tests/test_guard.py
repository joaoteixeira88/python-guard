import pytest

from exception.argument_empty_exception import ArgumentEmptyException
from exception.argument_not_equal_exception import ArgumentNotEqualException
from exception.argument_not_instance_of_exception import ArgumentNotInstanceOfException
from exception.argument_not_null_exception import ArgumentNotNullException
from exception.argument_null_exception import ArgumentNullException
from exception.argument_out_of_range_exception import ArgumentOutOfRangeException
from guard.guard import Guard


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

    @pytest.mark.parametrize(
        "param, param_name, message, expected",
        [
            (1, "test", "test cannot be null", pytest.raises(ArgumentNotNullException)),
            ([], "test", None, pytest.raises(ArgumentNotNullException))
        ]
    )
    def test_Null_InputParameter_RaiseArgumentNotNullException(self, param, param_name, message, expected):
        with expected:
            Guard.Null(param, param_name, message)

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
    def test_NotAny_InputParameter_ExpectedResult(self, param, param_name, message, expected):
        with expected:
            Guard.NotAny(param, param_name, message)

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
    def test_NotEqualTo_NotEqualParameter_RaisedArgumentNotEqualException(self, param, value, message, expected):
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
    def test_NotEqualTo_IqualParameter_ExpectedResult(self, param, value):
        Guard.NotEqualTo(param, value)

    @pytest.mark.parametrize(
        "param, value, param_name, message, expected",
        [
            (2, 1,  None, "param cannot be greater than 1.", pytest.raises(ArgumentOutOfRangeException)),
            (5.43345, 3.3434, "test", "test cannot be greater than 3.3434.", pytest.raises(ArgumentOutOfRangeException)),
        ]
    )
    def test_NotGreaterThan_GreaterThanThreshsold_RaisedArgumentOutOfRangeException(self, param, value, param_name,
                                                                                  message, expected):
        with expected:
            Guard.NotGreaterThan(param, value, param_name, message)

    @pytest.mark.parametrize(
        "param, value",
        [
            (1, 2),
            (3.43345, 5.3434)
        ]
    )
    def test_NotGreaterThan_LowerThanThreshsold_RaisedArgumentOutOfRangeException(self, param, value):
        Guard.NotGreaterThan(param, value)

    @pytest.mark.parametrize(
        "param, typeof, param_name, message, expected",
        [
            (2, str, None, "param is not from str.", pytest.raises(ArgumentNotInstanceOfException)),
            ([], dict, None, "param is not from dict.", pytest.raises(ArgumentNotInstanceOfException)),
            ("test", bool, None, "param is not from str.", pytest.raises(ArgumentNotInstanceOfException))
        ]
    )
    def test_IsNotInstanceOfType_InvalidType_RaisedArgumentNotInstanceOfExceptionn(self, param, typeof, param_name,
                                                                                   message, expected):
        with expected:
            Guard.IsNotInstanceOfType(param, typeof, param_name, message)

    @pytest.mark.parametrize(
        "param, value, param_name, message, expected",
        [
            (1, 2, None, "param cannot be greater than 1.", pytest.raises(ArgumentOutOfRangeException)),
            (
            3.43345, 5.3434, "test", "test cannot be greater than 3.3434.", pytest.raises(ArgumentOutOfRangeException)),
        ]
    )
    def test_NotLessThan_LessThanThreshsold_RaisedArgumentOutOfRangeException(self, param, value, param_name,
                                                                                    message, expected):
        with expected:
            Guard.NotLessThan(param, value, param_name, message)

    @pytest.mark.parametrize(
        "param, value",
        [
            (2, 1),
            (5.43345, 3.3434)
        ]
    )
    def test_NotLessThan_GreaterThanThreshsold_RaisedArgumentOutOfRangeException(self, param, value):
        Guard.NotLessThan(param, value)