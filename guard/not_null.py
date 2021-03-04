from string import Template
from typing import Any

from exception.argument_null_exception import ArgumentNullException

NotNullMessageTemplate = '$var cannot be Null.'
GenericParameterName = 'parameter'


class Guard(object):
    @staticmethod
    def NotNull(param: Any, param_name: str, message=None) -> None:
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
            message = Template(NotNullMessageTemplate).substitute(param_name)

        if not param:
            raise ArgumentNullException(message)


# Guard.NotNull(None, "xxxx")