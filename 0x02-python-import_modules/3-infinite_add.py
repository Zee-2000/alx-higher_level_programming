#!/usr/bin/python3
if __name__ == "_main_":
    from sys import argv
    total = 0
    for i in range(len(argv) - 1):
        total += int(argv[i + 1])
    print("{}".format(total))