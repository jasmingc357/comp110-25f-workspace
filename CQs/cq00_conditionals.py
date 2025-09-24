"""First challenge question"""

__author__: str = "730620666"


def guess_a_number() -> None:
    """All inputs will be made by the user and nothing will be returned"""
    secret: int = 7
    x = input("Guess a number:")
    print("Your guess was " + str(x))

    if int(x) == secret:
        print("You got it!")
    elif int(x) < secret:
        print("Your guess was too low! The secret number is", secret)
    elif int(x) > secret:
        print("Your guess was too high! The secret number is", secret)

    return None


# local variable for secret number uses an = sign

if __name__ == "__main__":
    guess_a_number()


# prompts user to guess a number and checks if it is equal to the secret number
