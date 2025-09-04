"""Decomposing a larger program into small subprograms"""

__author__: str = "730620666"


def main_planner(guests: int) -> None:
    """The main function for the tea party planner."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


# the main function calls all the other functions and prints the results


def tea_bags(people: int) -> int:
    """the number of guest attending the tea party."""
    return people * 2


# after this, test the progam in trailhead


def treats(people: int) -> int:
    """the number of treats needed for the tea party."""
    return int(tea_bags(people) * 1.5)


# data type return needs to be an int here, since it is being multiplied by a float


def cost(tea_count: int, treat_count: int) -> float:
    """the total cost of the tea party."""
    return (tea_count * 0.50) + (treat_count * 0.75)


# the cost of each tea bag is $0.50 and the cost of each treat is $0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
# this will prompt for the guest count, and give output of program after running it
