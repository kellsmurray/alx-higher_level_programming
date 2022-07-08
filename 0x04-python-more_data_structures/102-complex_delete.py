#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    new_dict = dict(a_dictionary)
    for k, v in list(new_dict.items()):
        if v == value:
            del new_dict[key]
    return (new_dict)
