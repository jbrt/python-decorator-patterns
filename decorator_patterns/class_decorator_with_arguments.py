#!/usr/bin/env python3


class ClassBasedDecoratorWithParams:

    def __init__(self, arg1, arg2):
        """
        Initialization (takes the arguments of the decorator)
        :param arg1: argument one
        :param arg2: argument two
        """
        print("Initialization of the decorator")
        print(f'Arguments for decorator: {arg1}, {arg2}')

    def __call__(self, fn, *args, **kwargs):
        """
        This method will take the argument for the decorated function
        AND THE FUNCTION TO DECORATE (difference between the previous decorator)
        :param fn: function to decorate
        :param args: (list)
        :param kwargs: (dict)
        :return: function decorated
        """
        print("__call__ method")

        def inner_function(*args, **kwargs):
            # Something before
            print("Function has been decorated.  Congratulations.")
            response = fn(*args, **kwargs)
            # Something after
            return response
        return inner_function


@ClassBasedDecoratorWithParams("arg1", "arg2")
def print_arguments(*args):
    for arg in args:
        print(arg)


if __name__ == '__main__':
    print_arguments(1, 2, 3)
