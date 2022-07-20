#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        quot = a / b
    except (TypeError, ValueError, ZeroDivisionError):
        quot = None
    finally:
        print("Inside result: {}".format(quot))
        print("{:d} / {:d} = {}".format(a, b, quot))
