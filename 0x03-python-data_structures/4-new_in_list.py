#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    my_list[:] = cp_list[:]
    if idx < 0 or idx > (len(my_list) - 1):
        return (cp_list)

    cp_list[idx] = element
    return (cp_list)
