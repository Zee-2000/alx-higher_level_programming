#!/usr/bin/python3
""" defines a string to json function"""
import json


def to_json_string(my_obj):
    """this function returns json representation to string"""
    return json.dumps(my_obj)