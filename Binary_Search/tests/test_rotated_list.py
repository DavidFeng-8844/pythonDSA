import pytest
import Binary_Search.source.rotated_list as rotated_list

test = {
    "test0": {
        "nums": [19, 25, 29, 3, 5, 6, 7, 9, 11, 14],
        "output": 3
    },
    "test1": {
        "nums": [4, 5, 6, 7, 8, 1, 2, 3],
        "output": 5
    },
    "test2": {
        "nums": [1, 2, 3],
        "output": 0
    },
    "test3": {
        'nums': [7, 3, 5],
        'output': 1
    },
    "test4": {
        "nums": [3, 4, 5, 6, 7, 8, 1],
        "output": 6
    },
    "test5": {
        "nums": [3, 5, 7, 8, 9, 10],
        "output": 0
    },
    "test6": {
        "nums": [],
        "output": -1
    },
    "test7": {
        "nums": [1],
        "output": 0
    },
}


@pytest.mark.parametrize("test_cases", test)
def test_count_rotation_linear(test_cases):
    result = rotated_list.count_rotations_linear(test[test_cases]["nums"])
    assert result == test[test_cases]["output"]


@pytest.mark.parametrize("test_cases", test)
def test_count_rotation_binary(test_cases):
    result = rotated_list.count_rotations_binary(test[test_cases]["nums"])
    assert result == test[test_cases]["output"]


@pytest.mark.parametrize("test_cases", test)
def test_count_rotation_generic(test_cases):
    result = rotated_list.count_rotations_generic(test[test_cases]["nums"])
    assert result == test[test_cases]["output"]
