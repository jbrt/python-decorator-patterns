#!/usr/bin/env python3


def decorator_with_argument(arg1, arg2):
    """
    Function decorator with arguments
    :param arg1: (int) first argument
    :param arg2: (int) second argument
    :return: function decorated
    """
    def inner_function(func_to_decorate):
        def wrapper(*args, **kwargs):
            print(f"Enter decorator with arguments: {arg1} & {arg2}")
            # Something before
            response = func_to_decorate(*args, **kwargs)
            # Something after
            return response
        return wrapper
    return inner_function


@decorator_with_argument("arg1", "arg2")
def print_arguments(*args):
    for arg in args:
        print(arg)


if __name__ == '__main__':
    print_arguments(1, 2, 3)
