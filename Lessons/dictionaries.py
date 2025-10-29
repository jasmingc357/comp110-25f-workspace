"""practice using basic dictionaries syntax"""

ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
print(ice_cream)

# this creats a new dictionary ... and literals are surrounded by {curly braces}


# to add an element to the dictionary
ice_cream["mint"] = 3  # this adds mint 3 times to the dictionary
print(ice_cream)

 
# to remove an element from the dictionary
ice_cream.pop("mint")  # this removes vanilla from the dictionary
print(ice_cream)
# pop is a method aka a function so it needs () and not []


# to access a value(definition) in the dictionary
print(ice_cream["chocolate"])  # this prints the value of chocolate which has 12 order

# to modify a value in the dictionary like 10 orders of vanilla
ice_cream["vanilla"] += 2  # this adds 2 more to the value
ice_cream["vanilla"] = 10  # this also sets the value to 10
print(ice_cream)


# to acess the length of how many key value pairs are in the dictionary
print(
    len(ice_cream)
)  # this prints 3 because there are 3 key (chocolate, vanilla and strawberry)


# new boolean expression to check if a key is in the dictionary
print("chocolate" in ice_cream)  # this prints True
print("mint" in ice_cream)  # this prints False


# now check if a key is in the dictionary but also
# reply with a response (making it a conditional)
if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("no orders of mint!")


def grade_bump(gradebook: dict[str, str], student: str) -> None:
    """bumps up a student grade"""
    if gradebook[student] == "A":
        # this access the student grade.. and if its A .. it will be updated to A+
        gradebook[student] = "A+"
    else:
        gradebook[student] = "A"


gradebook: dict[str, str] = {"alyssa": "A", "luke": "B"}
grade_bump(gradebook, "alyssa")
grade_bump(gradebook, "luke")
print(gradebook)


ice_cream["pecan"]  # this is gonna text.. to see what type of error occurs
# its a keyerror
