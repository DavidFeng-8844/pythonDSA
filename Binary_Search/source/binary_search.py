import pytest


def test_location(cards, query, mid):
    print("mid: ", mid, "mid number: ", cards[mid])
    if cards[mid] == query:
        if mid - 1 >= 0 and cards[mid - 1] == query:
            return "left"
        else:
            return "found"
    elif cards[mid] < query:
        return "left"
    else:
        return "right"


def binary_search(**pair):
    lo, hi = 0, len(pair["cards"]) - 1
    while lo <= hi:
        print("lo: ", lo, "hi: ", hi)
        mid = (lo + hi) // 2
        result = test_location(pair["cards"], pair["query"], mid)
        if result == "found":
            return mid
        elif result == "left":
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


def general_binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == "found":
            return mid
        elif result == "left":
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


def general_nested_binary_search(**pair):
    def condition(mid):
        print("mid: ", mid, "mid number: ", pair["cards"][mid])
        if pair["cards"][mid] == pair["query"]:
            if mid - 1 >= 0 and pair["cards"][mid - 1] == pair["query"]:
                return "left"
            else:
                return "found"
        elif pair["cards"][mid] < pair["query"]:
            return "left"
        else:
            return "right"
    return general_binary_search(0, len(pair["cards"]) - 1, condition)