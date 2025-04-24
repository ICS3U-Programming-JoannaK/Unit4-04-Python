#!/usr/bin/env python3

# Created by: Joanna Keza
# Date: April 23, 2025
# This program catches erroneous input
# and uses a while true loop

import random


def main():
    generated_number = random.randint(0, 9)

    while True:
        user_string = input("Enter your number:")
        try:
            user_integer = int(user_string)
            if user_integer >= 0 and user_integer <= 9:
                if user_integer == generated_number:
                    print("{} is correct".format(user_integer))
                    break
                else:
                    print("{} is not correct, try again".format(user_integer))
            else:
                print("{} is not valid.".format(user_integer))
        except Exception:
            print("{} is not valid, please enter a number.".format(user_string))


if __name__ == "__main__":
    main()
