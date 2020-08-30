#!/usr/bin/env python3


class ClassBasedDecorator:
    """
    A class decorator without arguments
    """

    def __init__(self, func_to_decorate):
        """
        Initialization
        :param func_to_decorate: function to decorate
        """
        print("Initialization of the decorator")
        self.func_to_decorate = func_to_decorate

    def __call__(self, *args, **kwargs):
        """
        Method that will takes as arguments those from the function to decorate
        :param args: (list)
        :param kwargs: (dict)
        :return: function decorated
        """
        print("__class__ method of the decorator")
        # Something before
        response = self.func_to_decorate(*args, **kwargs)
        # Something after
        return response


@ClassBasedDecorator
def print_arguments(*args):
    for arg in args:
        print(arg)


if __name__ == '__main__':
    print_arguments(1, 2, 3)
