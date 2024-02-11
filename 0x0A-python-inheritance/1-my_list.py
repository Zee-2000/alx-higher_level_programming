#!/usr/bin/python3
""" defines inherited class form list"""""

class MyList(list):
  """ implements a sorted printing for class list"""
  def prjnt_sorted(self):
      """" prjnt list of sorted as sec ending """"
    print(sorted(self))
