"""a word guessing game"""

__author__: str = "730620666"


def input_guess(expected_length: int) -> str:
    """Prompts the user for a guess and checks to match expected length."""
    N: str = input(f"Enter a {expected_length} character word: ")
    while len(N) != expected_length:
        N = input(f"That wasn't {expected_length} chars! Try again: ")
    return N


# test in trailhead using (input_guess(#))


def contains_char(word: str, single_character: str) -> bool:
    """this will check to see if the single character is found in word parameter"""
    assert len(single_character) == 1, f"len('{single_character}') not 1"
    i: int = 0
    while i < len(word):
        if word[i] == single_character:
            return True
        i = i + 1
    return False


def emojified(guess: str, secret: str) -> str:
    """this will compare the parameters and a string of emojis will return"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002b1c"
    GREEN_BOX: str = "\U0001f7e9"
    YELLOW_BOX: str = "\U0001f7e8"
    # local variables above are the color of boxes that will show up
    i: int = 0
    box_color: str = ""
    while i < len(secret):
        if (
            guess[i] == secret[i]
        ):  # this checks for if both index numbers match to the exact character
            box_color = box_color + GREEN_BOX
        else:
            # this will check if the character is still in the word,
            # but not matched index
            if contains_char(secret, guess[i]) is True:
                box_color = box_color + YELLOW_BOX
            else:  # white tells us if character is not found at all
                box_color = box_color + WHITE_BOX
        i = i + 1  # this reenters the loop until the length of the word is reached
    return box_color


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1  # this is the starting turn number
    won: bool = False
    # will be used to check if the user won, because its said later not won

    while turn <= 6 and not won:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            won = True
        turn = turn + 1
    if not won:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
