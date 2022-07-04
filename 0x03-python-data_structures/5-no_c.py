#!/usr/bin/python3

def no_c(my_string):
    new_list = list(my_string)
    new_string = ""
    for i in new_list:
        if i == 'c' or i == 'C':
            del i
    return (new_string)
