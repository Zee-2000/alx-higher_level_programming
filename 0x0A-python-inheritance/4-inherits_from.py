#!/usr/bin/python3
"""
  this module defines a class-function checking if an object is an instance.
  the object is an instance of a class that inherited
  (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """Checks if an object is an instance or inherited instance of a class

    Args:
        obj (unknown): The object to check.
        a_class (type): The class to match the type of obj to.

    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    return (isinstance(obj, a_class) and type(obj) is not a_class)
