from string import Template

from exception.invalid_number_exception import InvalidNumberxception
from guard.helpers import get_message, get_param_name
from constants.templates import Templates
from exception.argument_out_of_range_exception import ArgumentOutOfRangeException

GenericParameterName = 'parameter'


def not_greater_than(param: int, threshold: int, param_name: str = None, message=None):
    """
    Guards the specified :param param from being greater than the specified param thershold by throwing an
    exception of type ArgumentOutOfRangeException with a specific :param message when the precondition
    has not been met.
    :param param: The param to be checked
    :param threshold: The threshold against which the param will be checked
    :param param_name: The name of the param to be checked, that will be included in the exception
    :param message: The message that will be included in the exception
    """

    param_name = get_param_name(param_name)
    message = message or get_message(template=Templates.NotGreaterThanMessage, param_name=param_name, valuegi=threshold)

    if param > threshold:
        raise ArgumentOutOfRangeException(message=message)


def not_less_than(param: int, threshold: int, param_name: str = None, message=None):
    """
    Guards the specified :param param from being less than the specified param threshold by throwing an
    exception of type ArgumentOutOfRangeException with a specific :param message when the precondition
    has not been met.
    :param param: The param to be checked
    :param threshold: The threshold against which the param will be checked
    :param param_name: The name of the param to be checked, that will be included in the exception
    :param message: The message that will be included in the exception
    """

    param_name = get_param_name(param_name)
    message = message or get_message(template=Templates.NotLessThanMessage, param_name=param_name, value=threshold)

    if param < threshold:
        raise ArgumentOutOfRangeException(message=message)

def not_negative(param: int, param_name: str = None, message=None):
    """
    Guards the specified :param param from being negative by throwing an
    exception of type ArgumentOutOfRangeException with a specific :param message when the precondition
    has not been met.
    :param param: The param to be checked
    :param param_name: The name of the param to be checked, that will be included in the exception
    :param message: The message that will be included in the exception
    """
    
    param_name = get_param_name(param_name)
    message = message or get_message(template=Templates.NotLessThanMessage, param_name=param_name)

    if param < 0:
        raise ArgumentOutOfRangeException(message=message)

def is_odd(param:int, param_name: str = None, message=None):
    """
    Guards the specified :param param from being a even number by throwing an
    exception of type InvalidNumberxception with a specific :param message when the precondition
    has not been met.
    :param param: The param to be checked
    :param param_name: The name of the param to be checked, that will be included in the exception
    :param message: The message that will be included in the exception
    """
    param_name = get_param_name(param_name)
    message = message or get_message(template=Templates.NotLessThanMessage, param_name=param_name)
    
    if param % 2 !=0:
        raise InvalidNumberxception(message=message)


def is_even(param: int, param_name: str = None, message=None):
    """
    Guards the specified :param param from being a odd number by throwing an
    exception of type InvalidNumberxception with a specific :param message when the precondition
    has not been met.
    :param param: The param to be checked
    :param param_name: The name of the param to be checked, that will be included in the exception
    :param message: The message that will be included in the exception
    """
    param_name = get_param_name(param_name)
    message = message or get_message(template=Templates.NotLessThanMessage, param_name=param_name)

    if param % 2 == 0:
        raise InvalidNumberxception(message=message)
