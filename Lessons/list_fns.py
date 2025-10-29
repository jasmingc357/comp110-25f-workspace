"""write three functions that operate on lists: oct. 20th TUESDAY """

def get_first(list_name: list[str]) -> str: 
    """returns the first element of a list"""
    if len(list_name) ==0 : 
        return ""
    return list_name[0] #this is subscription notation


def remove_first(list_name: list[str]) -> None: 
    """removes the first element AND doesnt return anything, so use return type None"""
    if len(list_name) > 0:
        list_name.pop(0) 


def get_and_remove_first(list_name: list[str]) -> str: 
    """ this will return the first element and also remove it from the list"""
    first: str = list_name[0]
    list_name.pop(0)
    return first
# Example usage: that with get the first element and remove it from a list too 

my_list = ["apple", "banana", "cherry"]
print(get_and_remove_first(my_list))            # Output: apple

