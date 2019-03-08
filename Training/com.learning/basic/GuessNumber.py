__author__ = 'aganiger'

import random

random_number = random.randint(1, 100)


def guessnumber():
    while True:
        user_input = int(input("Guess number between 1 to 100\n"))
        if user_input > random_number:
            print("Oh guess lower")
        elif user_input < random_number:
            print("Hmm, Guess Higher")
        else:
            print("Yo, you got it right!!")
            break


def main():
    guessnumber()


if __name__ == '__main__':
    main()
