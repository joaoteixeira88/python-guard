from string import Template

from constants.templates import Templates
from exception.argument_not_equal_exception import ArgumentNotEqualException
from exception.no_such_element_exception import NoSuchElementException
from guard.configurations import T, GenericParameterName


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
        raise ArgumentNotEqualException(message=message)


def NotIn(param: T, value: T, param_name: str = None, message=None):
    """
    Guards the specified :param param from not having specified value by throwing an exception of type
    NoSuchElementException with a specific :param message when the precondition has not been met
    :param value: Value to compare
    :param param: The param to be checked
    :param param_name: The name of the param to be checked, that will be included in the exception
    :param message: The message that will be included in the exception
    """

    if not param_name:
        param_name = GenericParameterName

    if not message:
        message = Template(Templates.NotInMessage).substitute(var=param_name)

    if value not in param:
        raise NoSuchElementException(message=message)
