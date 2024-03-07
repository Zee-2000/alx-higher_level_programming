#!/usr/bin/python3
"""JSON serilization of an object
Args:
obj(class) : an instance of class"""

def class_to_json(obj):
    """ Write a function that returns
    the dictionary description with simple data structure """
    
    return obj.__dict__