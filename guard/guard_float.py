import math
from string import Template

from constants.templates import Templates
from exception.argument_exception import ArgumentException
from guard.configurations import GenericParameterName


def not_infinity_number(param: float, param_name: str = None, message=None):
    """
    Guards the specified :param param from being an infinity number by throwing an exception of type
    ArgumentException with a specific :param message when the precondition has not been met
    :param param: The param to be checked
    :param param_name: The name of the param to be checked, that will be included in the exception
    :param message: The message that will be included in the exception
    """

    if not param_name:
        param_name = GenericParameterName

    if not message:
        message = Template(template=Templates.InfinityNumberMessage).substitute(var=param_name)

    if math.isinf(param):
        raise ArgumentException(message=message)


def is_infinity_number(param: float, param_name: str = None, message=None):
    """
    Guards the specified :param param from not being an infinity number by throwing an exception of type
    ArgumentException with a specific :param message when the precondition has not been met
    :param param: The param to be checked
    :param param_name: The name of the param to be checked, that will be included in the exception
    :param message: The message that will be included in the exception
    """

    if not param_name:
        param_name = GenericParameterName

    if not message:
        message = Template(template=Templates.NotInfinityNumberMessage).substitute(var=param_name)

    if not math.isinf(param):
        raise ArgumentException(message=message)


def not_nan(param: float, param_name: str = None, message=None):
    """
    Guards the specified :param param from being a nan (not a number) by throwing an exception of type
    ArgumentException with a specific :param message when the precondition has not been met
    :param param: The param to be checked
    :param param_name: The name of the param to be checked, that will be included in the exception
    :param message: The message that will be included in the exception
    """

    if not param_name:
        param_name = GenericParameterName

    if not message:
        message = Template(template=Templates.NotNaNMessage).substitute(var=param_name)

    if math.isnan(param):
        raise ArgumentException(message=message)


def is_nan(param: float, param_name: str = None, message=None):
    """
    Guards the specified :param param from not being a nan (not a number) by throwing an exception of type
    ArgumentException with a specific :param message when the precondition has not been met
    :param param: The param to be checked
    :param param_name: The name of the param to be checked, that will be included in the exception
    :param message: The message that will be included in the exception
    """

    if not param_name:
        param_name = GenericParameterName

    if not message:
        message = Template(template=Templates.NaNMessage).substitute(var=param_name)

    if not math.isnan(param):
        raise ArgumentException(message=message)
