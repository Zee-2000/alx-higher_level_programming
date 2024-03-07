#!/usr/bin/python3
"""Defines a file-reading function"""
import json

def load_from_json_file(filename):
    """Creates an object from JSON"""
    with open(filename) as f:
        return json.load(f)