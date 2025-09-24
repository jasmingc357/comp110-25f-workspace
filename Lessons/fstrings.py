"""f-string positional argument practice"""


def get_class(subject: str, num: int) -> None:
    """Prints out a class name and number using an f-string."""
    print(f"I'm taking {subject} {num}.")


get_class("comp", 455)
# this is positional agurment calling

get_class(subject="comp", num=455)
# this is keyword argument calling
