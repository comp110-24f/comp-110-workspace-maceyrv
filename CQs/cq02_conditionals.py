"""The goal of this program is to practice with conditionals, local variables, and user input by creating a guessing game program"""

__author__: str = "730715418"


def guess_a_number() -> None:
    secret: int = 7

    guess = int(input("Guess a number:"))
    print("Your guess was: " + str(guess))

    if guess == secret:
        print("You got it!")
    elif guess < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
