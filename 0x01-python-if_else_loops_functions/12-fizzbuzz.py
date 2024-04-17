#!/usr/bin/python3
def fizzbuzz():
    for Number in range(1, 101):
        if Number % 3 == 0 and Number % 5 == 0:
            print("FizzBuzz ", end="")
        elif Number % 3 == 0:
            print("Fizz ", end="")
        elif Number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(Number), end="")
