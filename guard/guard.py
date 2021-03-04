from string import Template
from typing import TypeVar, Any
from collections.abc import Iterable

from exception.argument_empty_exception import ArgumentEmptyException
from exception.argument_not_equal import ArgumentNotEqualException
from exception.argument_null_exception import ArgumentNullException

NotAnyMessageTemplate = '$var cannot be empty (should contain at least one element).'
NotEqualMessageTemplate = 'Equality precondition not met.'
NotNullMessageTemplate = '$var cannot be Null.'

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
            message = Template(NotAnyMessageTemplate).substitute(var=param_name)

        if not param or len(param_name) == 0:
            raise ArgumentEmptyException(message)

    @staticmethod
    def NotNull(param: Any, param_name: str = None, message=None) -> None:
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
            message = Template(NotNullMessageTemplate).substitute(var=param_name)

        if not param:
            raise ArgumentNullException(message)

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
            message = NotAnyMessageTemplate

        if param != value:
            raise ArgumentNotEqualException(message)
