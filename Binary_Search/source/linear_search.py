import pytest

"""This is a correct linear search function that can pass all the test
    and check if we reach the end of the loop """


def linear_search(**pair):
    position = 0
    while position < len(pair["cards"]):
        if pair["cards"][position] == pair["query"]:
            return position
        position += 1
    return -1
