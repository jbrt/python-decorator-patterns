#!/usr/bin/env python3


def decorator_without_argument(func_to_decorate):
    """
    Function decorator without argument
    :param func_to_decorate: function to decorate
    :return: function decorated
    """
    def inner_function(*original_args, **original_kwargs):
        print("Enter decorator")
        # Something before
        response = func_to_decorate(*original_args, **original_kwargs)
        # Something after
        return response
    return inner_function


@decorator_without_argument
def print_arguments(*args):
    for arg in args:
        print(arg)


if __name__ == '__main__':
    print_arguments(1, 2, 3)
