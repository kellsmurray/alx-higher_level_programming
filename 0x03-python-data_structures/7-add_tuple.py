#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a[0] == 0 or tuple_a[1] == 0:
        return (0)
    if tuple_b[0] == 0 or tuple_b[1] == 0:
        return (0)
    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    print("{:d}".format(new_tuple))
