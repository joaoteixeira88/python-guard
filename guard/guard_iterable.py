from collections.abc import Iterable
from string import Template

from constants.templates import Templates
from exception.argument_empty_exception import ArgumentEmptyException
from exception.argument_exception import ArgumentException
from guard.configurations import GenericParameterName


def not_any(param: Iterable, param_name: str = None, message=None) -> None:
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


def min_count(param: Iterable, threshold: int, param_name: str = None, message=None) -> None:
    """
    Guards the specified :param param from containing less elements than :param threshold by throwing
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


def contains_duplicated(param: Iterable, message=None):
    """
    Guards the specified :param param from having duplicated values by throwing
    an exception of type ArgumentException with a specific :param message when the precondition has not been met
    :param param: The param to be checked
    :param message: The message that will be included in the exception
    """

    if not message:
        message = Template(Templates.ContainDuplicatedMessage).substitute()

    if len(param) != len(set(param)):
        raise ArgumentException(message)

