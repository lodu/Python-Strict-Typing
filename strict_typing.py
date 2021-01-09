from functools import wraps

# What to do when types do not match
def _strict_type_error(arg, actual_type, expected_type):
    raise TypeError(f"Argument: {arg} should be {actual_type} not {expected_type}")


# Explicit
def check_strict_typing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_param_dict = func.__annotations__
        func_param_list = list(func_param_dict.items())

        for index, arg in enumerate(args):
            func_param_type = func_param_list[index][1]
            if not isinstance(arg, (func_param_type, type(None))):
                _strict_type_error(arg, func_param_type, type(arg))

        for param_name, kwarg in kwargs.items():
            if func_param_dict.get(param_name) and not isinstance(
                kwarg, (func_param_dict[param_name], type(None))
            ):
                _strict_type_error(param_name, func_param_dict[param_name], type(kwarg))
        return func(*args, **kwargs)

    return wrapper


# List comprehension
# idk why you would use this tbh it makes the error ambiguous
def check_strict_typing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_param_dict = func.__annotations__
        func_param_list = list(func_param_dict.items())

        [
            _strict_type_error(arg, func_param_list[index][1], type(arg))
            for index, arg in enumerate(args)
            if not isinstance(arg, (func_param_list[index][1], type(None)))
        ]

        [
            _strict_type_error(param_name, func_param_dict[param_name], type(kwarg))
            for param_name, kwarg in kwargs.items()
            if func_param_dict.get(param_name)
            and not isinstance(kwarg, (func_param_dict[param_name], type(None)))
        ]

        return func(*args, **kwargs)

    return wrapper
