"""practice with booleans."""

# Write a function called check_first_letter that takes a input two strs: word and letter
# It should return “match!” if the first character of word is letter
# Otherwise, it should return “no match!”


def check_fisrt_letter(word: str, letter: str) -> str:
    """Check if the first letter of the word matches the given letter."""
    if word[0] == letter:
        return "match!"
    else:
        if word[0] != letter:
            return "no match!"
        # "no match!"


# print(check_fisrt_letter(word="hello", letter="h"))
# Should return True


# print(check_fisrt_letter(word="hello", letter="l"))


# Write a function called get_weather_report that takes weather: str as input
# and returns a str
# ● If weather is "rainy" or "cold", it should print "Bring a jacket!"
# ● If weather is "hot", it should print "Keep cool out there!"
# ● Otherwise, it should print "I don't recognize this weather."
# ● return the weather variable
# ● Call it with the input “cold” to see what you get!
# ● Now, use the input function to ask the user “What is the weather?” and pass
# that as the argument to get_weather_report


def get_weather_report(weather: str) -> str:
    """Get a weather report based on the input weather condition."""
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather


# get_weather_report("cold")

# get_weather_report(weather=input("What is the weather?"))


# practice defining the function again here!


def get_weather_report(weather: str) -> str:
    """this would check wether then give action for it depending on what it is."""
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I dont recognize this weather.")
    return weather


# get_weather_report(weather="cold")


# Now, use the input function to ask the user “What is the weather?” and pass
# that as the argument to get_weather_report

get_weather_report(weather=input("what is the weather?"))
