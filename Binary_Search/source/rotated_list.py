import pytest

""""This function is to receive a list of integers of lists obtained by rotating a sorted list by
    a certain number of times, the function should return the number of times the list was rotated(sorted means that
    the list is arranged in an increasing order). Rotated means that  removing the last element of the 
    list and adding it before the first element"""


def rotated_list(num):
    # create a variable to store the number of times the list was rotated
    count = 0
    # create a variable to store the index of the minimum element
    index = 0
    # create a variable to store the minimum element
    minimum = num[0]
    # loop through the list
    for i in range(len(num)):
        # check if the element is less than the minimum
        if num[i] < minimum:
            # update the minimum
            minimum = num[i]
            # update the index
            index = i
    # return the index
    return index
