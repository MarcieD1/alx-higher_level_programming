#!/usr/bin/python3
import random

def check_number(number):
    if number > 0:
        return f"{number} is positive"
    elif number == 0:
        return f"{number} is zero"
    else:
        return f"{number} is negative"

number = random.randint(-10, 10)
print(check_number(number))
