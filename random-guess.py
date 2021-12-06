"""
Author: Viernes, Michael
Submitted to: Mr. Danilo Madrigalejos
Submission date: December 11, 2021
Subject: Programming Logic and Design - HOMEWORK 08
"""

import random

def main():
    randgen_num = random.randint(0, 101)
    print("Random Generatad Number (0 - 100): ????")
    # print("The random number: " + str(randgen_num))
    while True:
        userinput = int(input("Guess the number: "))
        if userinput > randgen_num and userinput < 101:
            print("Your guess is a bit too high.")
        elif userinput < randgen_num:
            print("Youra guess is a bit too low.")
        elif userinput > 101:
            print("Aren't you out of bounds?")
        elif userinput == randgen_num:
            print("\nYou got it right!\n")
            return False
        
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
