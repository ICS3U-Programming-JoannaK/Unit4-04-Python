#!/usr/bin/env python3

# Created by: Joanna Keza
# Date: April 23, 2025
# This program catches erroneous input
# and uses a while true loop

import random


def main():
    # generates a random number between 0 and 9
    generated_number = random.randint(0, 9)

    # loop begins here
    while True:
        # Get user's number and assign it to a string
        user_string = input("Enter your number:")
        # CAST the string into an integer
        try:
            user_integer = int(user_string)
            # Checks if the number is in the needed range
            if user_integer >= 0 and user_integer <= 9:
                # Checks if user's number is the
                # same as the generated number
                if user_integer == generated_number:
                    # This displays when the user's guess is right
                    print("{} is correct".format(user_integer))
                    # Exits the loop
                    break
                else:
                    # This displays when the user's guess is wrong
                    print("{} is not correct, try again".format(user_integer))
            else:
                # This displays when the user's number is not in the range
                print("{} is not valid.".format(user_integer))
        except Exception:
            # Catches erroneous input
            print("{} is not valid, please enter a number.".format(user_string))


if __name__ == "__main__":
    main()
