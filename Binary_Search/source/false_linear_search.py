# import pytest


# This is a false linear search algorithm that might encounter list index out of range error
# The list is arranged in an decreasing order
def false_locate_cards(**pair):
    # create a variable of the value zero
    position = 0
    # Set up a loop for the iteration
    while True:
        # check if the element in the position is equal to the query
        if pair["cards"][position] == pair["query"]:
            # return the position
            return position
        # increment the position
        position += 1
        # check if we have reached the end of the list
        if position == len(pair["cards"]):
            return -1
