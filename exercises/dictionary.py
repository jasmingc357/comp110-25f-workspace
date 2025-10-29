"""Dctionary utility Functions exercise 4"""

__author__ = "730620666"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Invert the keys and values of the given dictionary"""
    inverted: dict[str, str] = {}  # new dictionary but flipped
    for key in dictionary:  # this is refering to the first str
        if dictionary[key] in inverted:
            # this is for the second str, when it becomes a key to not be a duplicate
            raise KeyError("thats a duplicate!")
        inverted[dictionary[key]] = key  # this is saying the value is now the old key
    return inverted


def favorite_color(names_and_fav_color: dict[str, str]) -> str:
    """returns most popular color and if tie, then returns the first popular color"""
    color_list: dict[str, int] = {}
    pop_color: str = ""
    zero = 0
    # an empty dict will keep track of the color along with # of times it appeared
    for name in names_and_fav_color:
        color = names_and_fav_color[name]
        if color in color_list:
            color_list[color] += 1
        else:
            color_list[color] = 1
    # color is now the new key , and for every one it counted for 1 when not duplicated
    for name in names_and_fav_color:
        color = names_and_fav_color[name]
        if color_list[color] > zero:
            pop_color = color
            zero = color_list[color]
    # the popular color is now replacing the color since it the larger value
    return pop_color
 

favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"})


def count(list_of_stuff: list[str]) -> dict[str, int]:
    """this will produce a dictionary with values associated are the counts"""
    count_dict: dict[str, int] = {}
    for item in list_of_stuff:
        if item in count_dict:  # if item is found then continue to add one
            count_dict[item] = (
                count_dict[item] + 1
            )  # this is when the value is found again
        else:  # this is for when the value is found just once
            count_dict[item] = 1
    return count_dict


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """this will produce a dictionary with
     values
    describing the times a letter appears
    in a list"""
    dictionary: dict[str, list[str]] = {}
    for word in words:  # this checks each word on the list
        first_letter = word[0].lower()  # checks the first letter
        if first_letter in dictionary:  # then for that letter
            dictionary[first_letter].append(
                word
            )  # you add that word to the letter identified before
        else:
            dictionary[first_letter] = [word]

    return dictionary


print(alphabetizer(["cat", "apple", "boy", "angry", "bad", "car"]))


def update_attendance(
    attendance_list: dict[str, list[str]],
    day: str,
    student: str,
) -> None:
    """this will mutate students that were counted for attendance on specific days"""
    if day in attendance_list:
        attendance_list[day].append(student)
        # this is mutating the day and student to the attendance list
    if day and student in attendance_list:
        attendance_list[day] = []
    else:
        attendance_list[day] = [student]

    return None


# attendance_list: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
# update_attendance(attendance_list, "Tuesday", "Vrinda")
# update_attendance(attendance_list, "Wednesday", "Kaleb")

# print(attendance_list)


print(invert({"Marc": "yellow", "Ezri": "pink", "Kris": "blue"}))
