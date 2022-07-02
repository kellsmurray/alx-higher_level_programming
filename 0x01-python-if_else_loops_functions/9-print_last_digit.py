#!/usr/bin/python3

def print_last_digit(number):
    str_num = str(num)
    if len(str_num) == 1:
        print("{}".format(int(str_num)))
    else:
        print("{}".format(int(str_num[-1])))
