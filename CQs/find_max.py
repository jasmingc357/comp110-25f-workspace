"""Unit test challenge question 03 max function."""

_author__: str = "730620666"


def find_and_remove_max(input_list: list[int]) -> int:
    """Finds and removes the maximum value from the input list."""

    # Return -1 for empty lists
    if input_list == []:
        return -1
 
    max_number: int = input_list[0]
    i: int = 0
    for x in input_list:
        if x > max_number:
            max_number = x

    while i < len(input_list):
        if input_list[i] == max_number:
            input_list.pop(i)
        else:
            i = i + 1

    # pop returns the removed value
    return max_number


a: list[int] = []
print(find_and_remove_max(a))  # Expected output: -1


b: list[int] = [10, 9, 8, 7, 10]
print(find_and_remove_max(b))

print(b)

c: list[int] = [9, 9, 8, 7]
print(find_and_remove_max(c))
print(c)
