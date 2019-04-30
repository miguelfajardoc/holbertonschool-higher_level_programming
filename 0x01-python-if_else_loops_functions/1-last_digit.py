#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0 and (number % 10 != 0):
    mod = (number % 10) - 10
else:
    mod = number % 10
if mod > 5:
    str = "and is greater than 5"
elif mod == 0:
    str = "and is 0"
else:
    str = "and is less than 6 and not 0"
print("Last digit of {:d} is {:d} {}".format(number, mod, str))
