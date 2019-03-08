__author__ = 'aganiger'

import random

number = random.randint(0, 100)


def guessNumber():
    while True:
        userNumber = int(input("Enter number between 0-100:\n"))
        if userNumber < number:
            print("Guess higher")
        elif userNumber > number:
            print("Guess Lower")
        else:
            print("Yah.. you got it")
            break


def main():
    guessNumber()


if __name__ == '__main__':
    main()

