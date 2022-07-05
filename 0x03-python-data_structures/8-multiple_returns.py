#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) == 0:
        fc = "None"
    else:
        fc = sentence[0]
    tup = (len(sentence), fc)
    print("{}".format(tup))
