"""
Author: Viernes, Michael
Submitted to: Mr. Danilo Madrigalejos
Submission date: December 11, 2021
Subject: Programming Logic and Design - HOMEWORK 08
"""

import math, random

def userinput(): # Using the same append method for inputs.
    guesses = []
    for i in range(3):
        guesses.append(int(input("Enter a number from 0-9: ")))
    return guesses
# End of function
    
def randomgen(): # Uses list comprehension in generating random numbers.
    random_nums  = [random.randint(0,10) for num in range(3)]
    return random_nums
    
# End of function

def validate(user_guess, gen_nums): # Matches the input if correct and returns user success.
    correct = 0
    
    print(f"""
    Here are my guesses: {user_guess}
    Here are the generated numbers: {gen_nums}
    """)
    
    for i in range(3):
        if user_guess[i] == gen_nums[i]:
            correct += 1
        else:
            continue

    if correct == 3: return True
    else: return False
    
# End of function
    
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
