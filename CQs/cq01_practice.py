"""Practice challeneg question ... so redo it here for practice."""


def num_instances(phrase: str, search_char: str) -> int:
    """this function should return the number of times search_char occurs in phrase."""
    count = 0
    x = 0
    while x < len(phrase):
        if phrase[x] == search_char:
            count = count + 1  # count will go up by one for every match
        x = x + 1  # to continue onto the next index/ letter
    return count


print(num_instances("Gavarrette", "t"))  # should print 1
