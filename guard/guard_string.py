import re
from string import Template

from constants.templates import Templates
from exception.argument_exception import ArgumentException
from exception.argument_out_of_range_exception import ArgumentOutOfRangeException
from guard.configurations import GenericParameterName
from guard.helpers import get_param_name, get_message


def email_not_valid(param: str, param_name: str = None, message=None):
    """
    Guards the specified :param param from being an invalid email by throwing an
    exception of type ArgumentException with a specific :param message when the precondition
    has not been met.
    :param param: The param to be checked
    :param param_name: The name of the param to be checked, that will be included in the exception
    :param message: The message that will be included in the exception
    """

    param_name = get_param_name(param_name)
    message = message or get_message(template=Templates.NotValidEmailMessage, param_name=param_name)

    if not re.match(r"[^@]+@[^@]+\.[^@]+", param):
        raise ArgumentException(message=message)


def length_not_greater_than(param: str, threshold: int, param_name: str = None, message=None):
    """
    Guards the specified :param param from having a length greater than the specified param threshold by throwing an
    exception of type ArgumentOutOfRangeException with a specific :param message when the precondition
    has not been met.
    :param param: The param to be checked
    :param threshold: The threshold against which the param will be checked
    :param param_name: The name of the param to be checked, that will be included in the exception
    :param message: The message that will be included in the exception
    """

    param_name = get_param_name(param_name)
    message = message or get_message(template=Templates.LengthNotGreaterThanMessage, param_name=param_name, value=threshold)

    if len(param) > threshold:
        raise ArgumentOutOfRangeException(message=message)


def length_not_less_than(param: str, threshold: int, param_name: str = None, message=None):
    """
    Guards the specified :param param from having a length less than the specified param threshold by throwing an
    exception of type ArgumentOutOfRangeException with a specific :param message when the precondition
    has not been met.
    :param param: The param to be checked
    :param threshold: The threshold against which the param will be checked
    :param param_name: The name of the param to be checked, that will be included in the exception
    :param message: The message that will be included in the exception
    """

    param_name = get_param_name(param_name)
    message = message or get_message(template=Templates.LengthNotLessThanMessage, param_name=param_name,
                                     value=threshold)

    if len(param) < threshold:
        raise ArgumentOutOfRangeException(message=message)


def is_not_white_space(param: str, param_name: str = None, message=None):
    """
    Guards the specified :param param from being a white space string by throwing an
    exception of type ArgumentException with a specific :param message when the precondition
    has not been met.
    :param param: The param to be checked
    :param param_name: The name of the param to be checked, that will be included in the exception
    :param message: The message that will be included in the exception
    """

    param_name = get_param_name(param_name)
    message = message or get_message(template=Templates.NotWhitespaceMessage, param_name=param_name)

    if len(param.strip()) <= 0:
        raise ArgumentException(message=message)
