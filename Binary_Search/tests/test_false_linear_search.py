import time

import pytest
import Binary_Search.source.false_linear_search as false_linear_search

# create a test case for the false linear search algorithm
tests = [{'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3},
         {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6},
         {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},
         {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},
         {'input': {'cards': [6], 'query': 6}, 'output': 0},
         {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
         {'input': {'cards': [], 'query': 7}, 'output': -1},
         {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3},
          'output': 7},
         {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
                    'query': 6},
          'output': 2}]


# This is a false linear search algorithm that might encounter list index out of range error
def test_false_linear_search_one(test_cases=None):
    if test_cases is None:
        test_cases = tests[0]
    result = false_linear_search.false_locate_cards(**test_cases["input"])
    assert result == test_cases["output"]


@pytest.mark.slow
def test_slow():
    time.sleep(2)
    result = false_linear_search.false_locate_cards(cards=[10, 7, 5, 3, 1], query=3)
    assert result == 3


def test_false_linear_search_two(test_cases=None):
    if test_cases is None:
        test_cases = tests[1]
    result = false_linear_search.false_locate_cards(**test_cases["input"])
    assert result == test_cases["output"]


# create a parametrized test case for the false linear search algorithm
@pytest.mark.parametrize("test_cases", tests)
def test_false_linear_search_parametrize(test_cases):
    result = false_linear_search.false_locate_cards(**test_cases["input"])
    assert result == test_cases["output"]
