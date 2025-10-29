"""Unit tests for my list functions """ 


from lessons.unit_tests.list_fns import get_first , remove_first, get_and_remove_first
#this imports the function from the other file


#unit tests to check return VALUE 

def test_get_first_use_case() -> None:
    """ blanks for now.... """
    example: list[str] = ["chair", "desk", "lamp"]
    assert get_first(example) == "chair"
    # assert is a way to check if something is true
    

def test_get_first_edge_case() -> None: 
    """ check that get_first returns empty string ... when given an empty list"""
    example: list[str] = []
    assert get_first(example) == "" # this will cause an index error since there is no first element
    # so lets for to get_first function and add the if statment for 0 length lists


# now lets write a test for how input is modified 
def test_remove_first_use_case() -> None: 
    """ check that reove_first removes the first element from a list"""
    example: list[str] = ["chair", "desk", "lamp"]
    remove_first(example)
    assert example == ["desk", "lamp"] # check that the list has been modified correctly
    # it shouldnt have chair anymore .. because it removed the first elemetn using pop 

def tets_remove_first_edge_case() -> None: 
    """ check that if we call it on an empty list, then nothing happens"""
    example: list [str] = [] 
    remove_first(example)
    assert example == []  # the list should still be empty
    # go edit the remove_first 



# unit test that checks how input is modified AND return value 
def test_get_and_remove_first_use_case () -> None: 
    """ Check that get_and_remove_first  both returns and removes the first element"""
    example: list[str] = ["chair", "desk", "lamp"]
    assert get_and_remove_first(example) == "chair"
    assert example == ["desk", "lamp"]

