#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    last = number % 10
else:
    last = ((number * -1) % 10) * -1

message = "Last digit of %d is %d and is" % (number, last)

if last > 5:
    print(message, "greater than 5")
if last == 0:
    print(message, "0")
if ((last < 6) & (last != 0)):
    print(message, "less than 6 and not 0")
