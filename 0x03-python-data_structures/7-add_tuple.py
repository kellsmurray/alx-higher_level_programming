#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a_length = len(tuple_a)
    tuple_b_length = len(tuple_b)

    if tuple_a_length == 0:
        a1 = 0
        a2 = 0
    elif tuple_a_length == 1:
        a1 = tuple_a[0]
        a2 = 0
    else:
        a1 = tuple_a[0]
        a2 = tuple_a[1]

    if tuple_b_length == 0:
        b1 = 0
        b2 = 0
    elif tuple_b_length == 1:
        b1 = tuple_b[0]
        b2 = 0
    else:
        b1 = tuple_b[0]
        b2 = tuple_b[1]

    new_tuple = (a1 + b1, a2 + b2)

    return (new_tuple)
