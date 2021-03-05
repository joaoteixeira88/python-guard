import re
from string import Template

from constants.templates import Templates
from exception.argument_exception import ArgumentException
from guard.configurations import GenericParameterName


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
