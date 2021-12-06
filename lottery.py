"""
Author: Viernes, Michael
Submitted to: Mr. Danilo Madrigalejos
Submission date: December 11, 2021
Subject: Programming Logic and Design - HOMEWORK 08
"""

import math, random

def userinput(): # Using the same append method for inputs.

    
def randomgen(): # Uses list comprehension in generating random numbers.


def validate(user_guess, gen_nums): # Matches the input if correct and returns user success.

    
def main():
    my_guess = userinput()
    is_valid = validate(my_guess, randomgen())
    print("The guesses are " + str(is_valid) + ".")
# End of function.

while True: # My template for usual main().
    main()
    quit = input("Quit (y/n): ")
    if quit is type(str):
        quit = quit.lower()
        print(quit)
    if (quit == 'y' or quit == 0):
        print("Closing...\n")    
        break
# End of Function.
