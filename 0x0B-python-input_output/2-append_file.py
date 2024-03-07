#!/usr/bin/python3
"""This module appends the text in utf-8 file
Args:
filename(str) : name of file
text(str) : text to append the file"""

def append_file(filename="", text=""):
    """A function that appends the text"""
    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)