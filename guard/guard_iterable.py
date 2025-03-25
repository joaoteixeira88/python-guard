from collections.abc import Iterable
from string import Template

from constants.templates import Templates
from exception.argument_empty_exception import ArgumentEmptyException
from exception.argument_exception import ArgumentException
from guard.configurations import GenericParameterName
from guard.helpers import get_param_name, get_message


def not_any(param: Iterable, param_name: str = None, message=None) -> None:
    """
    Guards the specified :param param from containing no elements by throwing an exception of type
    ArgumentEmptyException with a specific :param message when the precondition has not been met
    :param param: The param to be checked
    :param param_name: The name of the param to be checked, that will be included in the exception
    :param message: The message that will be included in the exception
    """

    param_name = get_param_name(param_name)
    message = message or get_message(template=Templates.NotAnyMessage, param_name=param_name)

    if not param or len(param) == 0:
        raise ArgumentEmptyException(message=message)


def min_count(param: Iterable, threshold: int, param_name: str = None, message=None) -> None:
    """
    Guards the specified :param param from containing less elements than :param threshold by throwing
    an exception of type ArgumentException with a specific :param message when the precondition has not been met
    :param param: The param to be checked
    :param threshold: The threshold against which the param will be checked
    :param param_name: The name of the param to be checked, that will be included in the exception
    :param message: The message that will be included in the exception
    """

    param_name = get_param_name(param_name)
    message = message or get_message(template=Templates.MinCountMessage, param_name=param_name, value=threshold)

    if len(param) < threshold:
        raise ArgumentException(message=message)


def contains_duplicated(param: Iterable, message=None):
    """
    Guards the specified :param param from having duplicated values by throwing
    an exception of type ArgumentException with a specific :param message when the precondition has not been met
    :param param: The param to be checked
    :param message: The message that will be included in the exception
    """

    message = message or get_message(template=Templates.ContainDuplicatedMessage)

    if len(param) != len(set(param)):
        raise ArgumentException(message=message)

