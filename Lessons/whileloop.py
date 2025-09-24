"""Whil Loop Statement"""


def find_low_card(cards: str) -> int:
    """Find Small Card by looping through a string number"""
    index: int = 0
    low_card: int = int(cards[0])
    while index < len(cards):
        if int(cards[index]) < low_card:
            low_card = int(cards[index])
        index = index + 1
    return low_card


print(find_low_card(cards="8675309"))
