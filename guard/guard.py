import re
from string import Template
from typing import TypeVar, Any
from collections.abc import Iterable

from constants.templates import Templates
from exception.argument_empty_exception import ArgumentEmptyException
from exception.argument_exception import ArgumentException
from exception.argument_not_equal_exception import ArgumentNotEqualException
from exception.argument_not_instance_of_exception import ArgumentNotInstanceOfException
from exception.argument_not_null_exception import ArgumentNotNullException
from exception.argument_null_exception import ArgumentNullException
from exception.argument_out_of_range_exception import ArgumentOutOfRangeException


GenericParameterName = 'parameter'


class Guard(object):
    T = TypeVar('T')

    @staticmethod
    def NotAny(param: Iterable, param_name: str = None, message=None) -> None:
        """
        Guards the specified :param param from containing no elements by throwing an exception of type
        ArgumentEmptyException with a specific :param message when the precondition has not been met
        :param param: The param to be checked
        :param param_name: The name of the param to be checked, that will be included in the exception
        :param message: The message that will be included in the exception
        """

        if not param_name:
            param_name = GenericParameterName

        if not message:
            message = Template(Templates.NotAnyMessage).substitute(var=param_name)

        if not param or len(param) == 0:
            raise ArgumentEmptyException(message)

    @staticmethod
    def MinCount(param: Iterable, threshold: int, param_name: str = None, message=None) -> None:
        """
        Guards the specified :param param from containing lesse elements than :param threshold by throwing
        an exception of type ArgumentException with a specific :param message when the precondition has not been met
        :param param: The param to be checked
        :param threshold: The threshold against which the param will be checked
        :param param_name: The name of the param to be checked, that will be included in the exception
        :param message: The message that will be included in the exception
        """

        if not param_name:
            param_name = GenericParameterName

        if not message:
            message = Template(Templates.MinCountMessage).substitute(var=param_name, value=threshold)

        if len(param) < threshold:
            raise ArgumentException(message)

    @staticmethod
    def NotNull(param: T, param_name: str = None, message=None) -> None:
        """
        Guards the specified :param param from being null by throwing an exception of type ArgumentNullException with
        a specific :param message when the precondition has not been met
        :param param: The param to be checked
        :param param_name: The name of the param to be checked, that will be included in the exception
        :param message: The message that will be included in the exception
        """

        if not param_name:
            param_name = GenericParameterName

        if not message:
            message = Template(Templates.NotNullMessage).substitute(var=param_name)

        if not param:
            raise ArgumentNullException(message)

    @staticmethod
    def Null(param: T, param_name: str = None, message=None) -> None:
        """
        Guards the specified :param param from not being null by throwing an exception of type
        ArgumentNotNullException with a specific :param message when the precondition has not been met
        :param param: The param to be checked
        :param param_name: The name of the param to be checked, that will be included in the exception
        :param message: The message that will be included in the exception
        """

        if not param_name:
            param_name = GenericParameterName

        if not message:
            message = Template(Templates.NotNullMessage).substitute(var=param_name)

        if param != None:
            raise ArgumentNotNullException(message)

    @staticmethod
    def NotEqualTo(param: T, value: T, message=None) -> None:
        """
        Guards the specified :param param from not being equal to the specified by throwing an exception of type
        ArgumentNotEqualException with a specific :param message when the precondition has not been met
        :param value: Value to compare
        :param param: The param to be checked
        :param message: The message that will be included in the exception
        """

        if not message:
            message = Templates.NotAnyMessage

        if param != value:
            raise ArgumentNotEqualException(message)

    @staticmethod
    def NotGreaterThan(param: int, threshold: int, param_name: str = None, message=None):
        """
        Guards the specified :param param from being greater than the specified param thershold by throwing an
        exception of type ArgumentOutOfRangeException with a specific :param message when the precondition
        has not been met.
        :param param: The param to be checked
        :param threshold: The threshold against which the param will be checked
        :param param_name: The name of the param to be checked, that will be included in the exception
        :param message: The message that will be included in the exception
        """

        if not param_name:
            param_name = GenericParameterName

        if not message:
            message = Template(Templates.NotGreaterThanMessage).substitute(var=param_name, value=threshold)

        if param > threshold:
            raise ArgumentOutOfRangeException(message)

    @staticmethod
    def NotLessThan(param: int, thershold: int, param_name: str = None, message=None):
        """
        Guards the specified :param param from being less than the specified param thershold by throwing an
        exception of type ArgumentOutOfRangeException with a specific :param message when the precondition
        has not been met.
        :param param: The param to be checked
        :param thershold: The threshold against which the param will be checked
        :param param_name: The name of the param to be checked, that will be included in the exception
        :param message: The message that will be included in the exception
        """

        if not param_name:
            param_name = GenericParameterName

        if not message:
            message = Template(Templates.NotLessThanMessage).substitute(var=param_name, value=thershold)

        if param < thershold:
            raise ArgumentOutOfRangeException(message)

    @staticmethod
    def IsNotInstanceOfType(param: T, typeof: Any,  param_name: str = None, message=None):
        """
        Guards the specified :param param type from being different from the :param typeof by throwing an
        exception of type ArgumentNotInstanceOfException with a specific :param message when the precondition
        has not been met.
        :param param: The param to be checked
        :param typeof: Object instance which the param will be checked
        :param param_name: The name of the param to be checked, that will be included in the exception
        :param message: The message that will be included in the exception
        """
        if not param_name:
            param_name = GenericParameterName

        if not message:
            message = Template(Templates.NotInstanceOfTypeMessage).substitute(var=param_name, type=typeof)

        if typeof(param) != typeof:
            raise ArgumentNotInstanceOfException(message)

    @staticmethod
    def EmailNotValid(param: str, param_name: str = None, message=None):
        """
        Guards the specified :param param from being an invalid email by throwing an
        exception of type ArgumentException with a specific :param message when the precondition
        has not been met.
        :param param: The param to be checked
        :param param_name: The name of the param to be checked, that will be included in the exception
        :param message: The message that will be included in the exception
        """
        if not param_name:
            param_name = GenericParameterName

        if not message:
            message = Template(Templates.NotValidEmailMessage).substitute(var=param_name)

        if not re.match(r"[^@]+@[^@]+\.[^@]+", param):
            raise ArgumentException(message)
