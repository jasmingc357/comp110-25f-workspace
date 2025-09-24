"""While loops challenge question."""

__author__: str = "730620666"


def num_instances(phrase: str, search_char: str) -> int:
    """counts the occurrences of search_charr in a phrase."""
    count = 0
    # count is the starting point
    i = 0
    # is the local variable that will track the index
    while i < len(phrase):
        if phrase[i] == search_char:
            count = count + 1
        i = i + 1
    return count


print(num_instances("yummy", "y"))  # should print 2
