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
    print("The random number: " + str(randgen_num))

        
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
