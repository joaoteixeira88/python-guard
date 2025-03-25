from string import Template

from guard.configurations import GenericParameterName


def get_param_name(param_name: str) -> str:
    return param_name or GenericParameterName

def get_message(template: str, param_name: str = None, **kwargs) -> str:
    """Substitutes template variables with provided values."""
    if not kwargs:
        return Template(template=template).substitute(var=param_name)

    if not param_name and not kwargs:
        return Template(template=template).substitute()

    return Template(template=template).substitute(var=param_name, **kwargs)