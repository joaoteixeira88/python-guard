from string import Template

from constants.templates import Templates
from exception.argument_not_null_exception import ArgumentNotNullException
from exception.argument_null_exception import ArgumentNullException
from guard.configurations import T, GenericParameterName


def NotNull(param: T, param_name: str = None, message=None) -> None:
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
        message = Template(Templates.NotNullMessage).substitute(var=param_name)

    if not param:
        raise ArgumentNullException(message)


def Null(param: T, param_name: str = None, message=None) -> None:
    """
    Guards the specified :param param from not being null by throwing an exception of type
    ArgumentNotNullException with a specific :param message when the precondition has not been met
    :param param: The param to be checked
    :param param_name: The name of the param to be checked, that will be included in the exception
    :param message: The message that will be included in the exception
    """

    if not param_name:
        param_name = GenericParameterName

    if not message:
        message = Template(Templates.NotNullMessage).substitute(var=param_name)

    if param != None:
        raise ArgumentNotNullException(message)
