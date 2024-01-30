# This is a python program that implement the binary search algorithm
import pytest

'''This function is an example of binary search but doesn't check if it is the first occurrence of the query'''


def false_binary_search(**pair):
    lo, hi = 0, len(pair["cards"]) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if pair["cards"][mid] == pair["query"]:
            return mid
        elif pair["cards"][mid] < pair["query"]:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1
