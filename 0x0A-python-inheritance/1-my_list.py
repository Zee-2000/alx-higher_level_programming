#!/usr/bin/python3
""" defines inherited class form list"""

class MyList(list):
    """ implements a sorted printing for class list"""
    def print_sorted(self):
        """ print list of sorted assecending """
        print(sorted(self))
