import pytest

from exception.argument_empty_exception import ArgumentEmptyException
from exception.argument_exception import ArgumentException
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
            (2, 1, None, "param cannot be greater than 1.", pytest.raises(ArgumentOutOfRangeException)),
            (
            5.43345, 3.3434, "test", "test cannot be greater than 3.3434.", pytest.raises(ArgumentOutOfRangeException)),
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
    def test_NotGreaterThan_LowerThanThreshold_RaisedArgumentOutOfRangeException(self, param, value):
        Guard.NotGreaterThan(param, value)

    @pytest.mark.parametrize(
        "param, typeof, param_name, message, expected",
        [
            (2, str, None, "parameter is not from type <class 'str'>.", pytest.raises(ArgumentNotInstanceOfException)),
            ([], dict, None, "parameter is not from type <class 'dict'>.", pytest.raises(ArgumentNotInstanceOfException)),
            ("test", bool, None, "parameter is not from type <class 'bool'>.", pytest.raises(ArgumentNotInstanceOfException))
        ]
    )
    def test_IsNotInstanceOfType_InvalidType_RaisedArgumentNotInstanceOfException(self, param, typeof, param_name,
                                                                                  message, expected):
        with expected as err:
            Guard.IsNotInstanceOfType(param=param, typeof=typeof, param_name=param_name)

        assert message in str(err.value)

    @pytest.mark.parametrize(
        "param, value, param_name, message, expected",
        [
            (1, 2, None, "parameter cannot be greater than 1.", pytest.raises(ArgumentOutOfRangeException)),
            (
                    3.43345, 5.3434, "test", "test cannot be greater than 3.3434.",
                    pytest.raises(ArgumentOutOfRangeException)),
        ]
    )
    def test_NotLessThan_LessThanThreshold_RaisedArgumentOutOfRangeException(self, param, value, param_name,
                                                                             message, expected):
        with expected as err:
            Guard.NotLessThan(param=param, thershold=value, param_name=param_name)

        assert message in str(err.value)

    @pytest.mark.parametrize(
        "param, value",
        [
            (2, 1),
            (5.43345, 3.3434)
        ]
    )
    def test_NotLessThan_GreaterThanThreshold_RaisedArgumentOutOfRangeException(self, param, value):
        Guard.NotLessThan(param=param, thershold=value)

    @pytest.mark.parametrize(
        "param, param_name, message, expected",
        [
            ("x.pt", None, "parameter is not a valid email.", pytest.raises(ArgumentException)),
            ("xxx@aa", None, "parameter is not a valid email.", pytest.raises(ArgumentException)),
            ("@", None, "parameter is not a valid email.", pytest.raises(ArgumentException)),
            ("xxxxx", None, "parameter is not a valid email.", pytest.raises(ArgumentException))
        ]
    )
    def test_EmailNotValid_InvalidEmail_RaisedArgumentException(self, param, param_name, message, expected):
        with expected as err:
            Guard.EmailNotValid(param=param, param_name=param_name)

        assert message in str(err.value)

    @pytest.mark.parametrize(
        "param, value, param_name, message, expected",
        [
            ([], 2, None, "parameter must have at least 2 elements.", pytest.raises(ArgumentException)),
            ({"a": 1}, 2, None, "parameter must have at least 2 elements.", pytest.raises(ArgumentException)),
            ({1, 2, 3}, 20, None, "parameter must have at least 20 elements.", pytest.raises(ArgumentException))
        ]
    )
    def test_NotLessThan_LessThanThreshold_RaisedArgumentOutOfRangeException(self, param, value, param_name,
                                                                             message, expected):
        with expected as err:
            Guard.MinCount(param=param, threshold=value, param_name=param_name)

        assert message in str(err.value)
