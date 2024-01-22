#!/usr/bin/python3
def safe_print_list_intergers(my_list=[], x=0):
    count = 0
    try:
        for element in my_list:
            if count < x and isinstance(element, int):
                print("{:d}".format(element), end=' ')
                count+=1
            print()
    except:
        pass
    return count