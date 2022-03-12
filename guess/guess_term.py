from random import randint


def create_number(low=0, high=100):
    return randint(low, high)


def question():
    answer = input("Guess a number: ")
    return int(answer)


def validate_quess(n, guess):
    if guess == n:
        return True, "YEAH"
    elif guess > n:
        return False, "To high, try again"
    elif guess < n:
        return False, "To low, try again"


def main():
    n = create_number()
    counter = 1
    while True:
        answer = question()
        correct, s = validate_quess(n, answer)
        if correct:
            print(f"You guessed it in {counter} guesses")
            break
        else:
            print(s)
        counter += 1


if __name__ == "__main__":
    main()
