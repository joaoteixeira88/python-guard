from string import Template
from typing import Any

from constants.templates import Templates
from exception.argument_not_instance_of_exception import ArgumentNotInstanceOfException
from guard.configurations import T, GenericParameterName


def is_not_instance_of_type(param: T, typeof: Any, param_name: str = None, message=None):
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
        message = Template(template=Templates.NotInstanceOfTypeMessage).substitute(var=param_name, type=typeof)

    if typeof(param) != typeof:
        raise ArgumentNotInstanceOfException(message=message)

