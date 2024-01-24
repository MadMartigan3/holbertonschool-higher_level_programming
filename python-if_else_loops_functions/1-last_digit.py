#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digits = abs(number) % 10

print("Last digit of", number, "is", last_digits, end="")

if last_digits > 5:
    print(" greater than 5")
elif last_digits == 0:
    print(" and is 0")
else:
    print(" less than 6 and not 0")
