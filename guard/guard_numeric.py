from string import Template

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

    if not param_name:
        param_name = GenericParameterName

    if not message:
        message = Template(template=Templates.NotGreaterThanMessage).substitute(var=param_name, value=threshold)

    if param > threshold:
        raise ArgumentOutOfRangeException(message=message)


def not_less_than(param: int, thershold: int, param_name: str = None, message=None):
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
        message = Template(template=Templates.NotLessThanMessage).substitute(var=param_name, value=thershold)

    if param < thershold:
        raise ArgumentOutOfRangeException(message=message)

