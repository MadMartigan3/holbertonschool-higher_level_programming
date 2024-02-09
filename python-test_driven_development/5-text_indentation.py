#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    last_char_special = False

    for char in text:
        if char in ['.', '?', ':']:
            if not last_char_special:
                print("\n")
            print(char + "\n\n", end="")
            last_char_special = True
        else:
            print(char, end="")
            last_char_special = False
