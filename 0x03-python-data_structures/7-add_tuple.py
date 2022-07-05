#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        tupl_a[0] = 0
        tupl_a[1] = 0
    elif len(tuple_a) == 1:
        tupl_a[0] = tuple_a[0]
        tupl_a[1] = 0
    else:
        tupl_a[0] = tuple_a[0]
        tupl_a[1] = tuple_a[1]

    if len(tuple_b) == 0:
        tupl_b[0] = 0
        tupl_b[1] = 0
    elif len(tuple_b) == 1:
        tupl_b[0] = tuple_b[0]
        tupl_b[1] = 0
    else:
        tupl_b[0] = tuple_b[0]
        tupl_b[1] = tuple_b[1]

    new_tuple = (tupl_a[0] + tupl_b[0], tupl_a[1] + tupl_b[1])
    print("{:d}".format(new_tuple))
