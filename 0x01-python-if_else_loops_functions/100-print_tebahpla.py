#!/usr/bin/python3

letter = 0
for char in range(122, 96, -1):
    if char % 2 == 0:
        letter = char
    else:
        letter = char - 32
print("{}".format(chr(letter)), end='')
