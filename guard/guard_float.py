import math
from string import Template

from constants.templates import Templates
from exception.argument_exception import ArgumentException
from guard.configurations import GenericParameterName


def IsNotInfinityNumber(param: float,  param_name: str = None, message=None):
    if not param_name:
        param_name = GenericParameterName

    if not message:
        message = Template(Templates.NotInfinityNumberMessage).substitute(var=param_name)

    if math.isinf(param):
        raise ArgumentException(message)
