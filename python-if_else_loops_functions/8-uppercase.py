#!/usr/bin/env python3
def uppercase(str):
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            print(chr(ord(char) - 32), end="")
        else:
            print(char, end="")
print()