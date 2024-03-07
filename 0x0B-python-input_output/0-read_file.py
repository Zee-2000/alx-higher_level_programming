#!/usr/bin/python3
"""This module has a function that reads a file 
UTF-8 and prints it"""

def read_file(filename=""):
    """function that reads a text file 
    (UTF8) and prints it to stdout"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")