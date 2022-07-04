#!/usr/bin/python3

def no_c(my_string):
    for i in range(len(my_string) - 1):
        if i == 'c' or i == 'C':
            del my_string[i]
    return (my_string)
