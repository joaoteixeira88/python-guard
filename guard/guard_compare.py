from constants.templates import Templates
from exception.argument_not_equal_exception import ArgumentNotEqualException
from guard.configurations import T


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
        raise ArgumentNotEqualException(message)
