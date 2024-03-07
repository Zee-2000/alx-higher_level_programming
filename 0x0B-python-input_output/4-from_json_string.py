#!/usr/bin/python3
"""Defines a string ffrom json function"""
import json

def from_json_string(my_obj):
    """returns python representation of json string"""
    return json.loads(my_obj)