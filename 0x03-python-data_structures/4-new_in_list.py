#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    print("{}".format(my_list))
    if idx < 0 or idx > (len(my_list) - 1):
        print("{}".format(my_list))
    else:
        my_list[idx] = element
        print("{}".format(my_list))
