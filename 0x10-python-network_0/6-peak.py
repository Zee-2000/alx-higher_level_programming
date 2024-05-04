#!/usr/bin/python3
"""Finding apeak in list of integers"""

def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    left = 0
    right = len(list_of_integers-1)
    
    while left <= right:
        middle = (left +(right - left) // 2)

        if middle > 0 and list_of_integers[middle] < list_of_integers[middle - 1]:
            right = middle - 1
        elif middle < len(list_of_integers) - 1 and list_of_integers[middle] < list_of_integers[middle + 1]:
            left = middle + 1
        else:
            return list_of_integers[middle]
         