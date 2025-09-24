"""practice cq00"""


def guess_a_number() -> None:
    """All inputs will be made by the user and nothing will be returned"""
    # signature was made to return None

    secret: int = 7
    x = input("Guess a number:")
    print("Your guess was " + str(x))

    if int(x) == secret:
        print("You Got it!")
    elif int(x) < secret:
        print("Your guess was too low!")
    elif int(x) > secret:
        print("Your guess was too high!")
    return None


if __name__ == "__main__":
    guess_a_number()
