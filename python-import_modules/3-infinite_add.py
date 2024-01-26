#!/usr/bin/python3
import sys

def additionner_arguments(*args):
    return sum(int(arg) for arg in args)

if __name__ == "__main__":
    arguments = sys.argv[1:]
    resultat = additionner_arguments(*arguments)
    print(resultat)
