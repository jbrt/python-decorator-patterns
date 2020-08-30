# Python decorator patterns

There is several way to implement the decorator pattern with Python language.
As far as I Know there is actually four way to do it depending if you want use 
classes or functions and if your decorator must take arguments or not. 

This repository act here as a memento.
**These solutions doesn't need to use functools.wraps().**

## Classes decorators

### Class decorator without arguments

With a class decorator that doesn't takes any arguments:

- reference of the decorated function/object is pass directly to __init__ method
- arguments for the decorated function/object is pass to __call__ method

````python
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
````

Usage of this decorator:

````python
@ClassBasedDecorator
def print_arguments(*args):
    for arg in args:
        print(arg)
````


### Class decorator with arguments

With a class decorator that takes arguments:

- arguments passed to decorator are handled by __init__ method
- reference of the decorated function/object is pass to __call__ method
- arguments for the decorated function/object is pass to __call__ method

```python
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
```

Usage:

````python
@ClassBasedDecoratorWithParams("arg1", "arg2")
def print_arguments(*args):
    for arg in args:
        print(arg)
````

## Functions decorators

### Functions decorator without arguments

With a function decorator that doesn't takes any arguments:

- reference of the decorated function/object is pass directly the decorator function
- arguments for the decorated function/object is pass to inner function

````python
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
````

Usage:

````python
@decorator_without_argument
def print_arguments(*args):
    for arg in args:
        print(arg)
````

### Functions decorator with arguments

With a function decorator that takes arguments:

- arguments passed to decorator are handled by decorator function directly
- reference of the decorated function/object is pass to inner function
- arguments for the decorated function/object is pass to wrapper function

````python
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
````

Usage:

````python
@decorator_with_argument("arg1", "arg2")
def print_arguments(*args):
    for arg in args:
        print(arg)
````