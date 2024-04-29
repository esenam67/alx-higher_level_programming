#!/usr/bin/python3
def uppercase(str):
    """ prints string in capital letter"""
    for x in str:
        if x >= 'a' and x <= 'z':
            x = ord(x) - 32
            print(x)
        else:
            print(x)
