#!/usr/bin/python3

def no_c(my_string):
    new_string = my_string[:]
    for i in range(len(new_string) - 1):
        if i == 'c' or i == 'C':
            del new_string[i]
    return (new_string)
