#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digits = abs(number) % 10
if number < 0:
    last_digits = -last_digits

print("Last digit of", number, "is", last_digits, end="")

if last_digits > 5:
    print(" and is greater than 5")
elif last_digits == 0:
    print(" and is 0")
else:
    print(" and is less than 6 and not 0")
