#!/usr/bin/python3

def uppercase(str):
    for i in str:
        if i >= 97 and i <= 122:
            upp_str = i - 32
        else:
            upp_str = i
        print(f"{}".format(upp_str))
