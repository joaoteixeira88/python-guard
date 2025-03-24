def get_param_name(param_name: str) -> str:
    """Returns a default parameter name if not provided."""
    return param_name or GenericParameterName

def get_message(template: Template, param_name: str, value=None) -> str:
    """Substitutes template variables with provided values."""
    return template.substitute(var=param_name, value=value)