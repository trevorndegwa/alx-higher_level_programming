#!/usr/bin/python3
def fizzbuzz():
    '''
    Print from 1 to 100 separated by space
    for 3-multiples, print Fizz
    for 5-multiples, print Buzz
    for multiples of both, print FizzBuzz
    '''
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
