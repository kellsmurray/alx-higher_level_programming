#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    else:
        maks = my_list[0]
        for i in range(1, len(my_list) - 1):
            if my_list[i] > maks:
                maks = my_list[i]
        return (maks)
