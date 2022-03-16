#!/usr/bin/env python

from random import randint


def create_number(low=0, high=100):
    return randint(low, high)


def question():
    answer = input("Guess a number: ")
    try:
        return int(answer)
    except ValueError:
        return False


def validate_quess(number, guess):
    if guess == number:
        return True, "YEAH"
    elif guess > number:
        return False, "To high, try again"
    return False, "To low, try again"


def main():
    number = create_number()
    counter = 1
    while True:
        answer = question()
        if not answer:
            continue
        correct, reply = validate_quess(number, answer)
        if correct:
            print(f"You guessed it in {counter} guesses")
            break
        print(reply)
        counter += 1


if __name__ == "__main__":
    main()
