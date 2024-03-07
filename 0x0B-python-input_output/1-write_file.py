#!/usr/bin/python3
"""Defines a file writing function"""

def write_file(filename="", text=""):
    """a function that writes a file utf-8 text
    Args:
    filename(str):name of file 
    text(str):The text to write the file"""
    
    with open(filename,"w", encoding='utf-8') as f:
        return f.write(text)