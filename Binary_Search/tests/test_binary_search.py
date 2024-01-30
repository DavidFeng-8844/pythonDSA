import pytest
import Binary_Search.source.binary_search as binary_search

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


@pytest.mark.parametrize("test_cases", tests)
def test_binary_search_one(test_cases):
    result = binary_search.binary_search(**test_cases["input"])
    assert result == test_cases["output"]


# create a parametrized test for the general binary search algorithm
@pytest.mark.parametrize("test_cases", tests)
def test_general_binary_search(test_cases):
    result = binary_search.general_nested_binary_search(**test_cases["input"])
    assert result == test_cases["output"]
