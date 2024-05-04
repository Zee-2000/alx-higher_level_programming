#!/usr/bin/python3
"""Finding apeak in list of integers"""

def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    left = 0
    right = len(list_of_integers-1)
    
    while left < right:
        middle = (left + right) // 2

        if list_of_integers[middle] < list_of_integers[middle + 1]:
            #peak is right
            left = middle + 1
        else:
            #peak is left
            right = middle
            
    return list_of_integers[left]