#!/usr/bin/python3
"""Defines JSON file-writing function"""
import json

def save_to_json_file(filename, my_obj):
    """Writes an object text file using JSON representation"""
    with open(filename, "w") as f:
        return json.dump(my_obj)