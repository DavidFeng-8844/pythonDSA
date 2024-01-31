import pytest
import Binary_Search.source.binary_search as bs

""""This function is to receive a list of integers of lists obtained by rotating a sorted list by
    a certain number of times, the function should return the number of times the list was rotated(sorted means that
    the list is arranged in an increasing order). Rotated means that  removing the last element of the 
    list and adding it before the first element"""


def count_rotations_linear(nums):
    position = 1  # What is the initial value of position?
    if len(nums) == 0:
        return -1
    while position < len(nums):  # When should the loop be terminated?
        # Success criteria: check whether the number at the current position is smaller than the one before it
        if nums[position] < nums[position - 1]:  # How to perform the check?
            return position
        # Move to the next position
        position += 1
    return 0  # What if none of the positions passed the check


def count_rotations_binary(nums):
    lo = 0
    hi = len(nums) - 1
    if len(nums) == 0:
        return -1  # What is the initial value of lo and hi?
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = nums[mid]
        # Uncomment the next line for logging the values and fixing errors.
        print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)

        if mid > 0 and mid_number < nums[mid - 1]:
            # The middle position is the answer
            return mid

        elif mid_number < nums[-1]:
            # Answer lies in the left half
            hi = mid - 1

        else:
            # Answer lies in the right half
            lo = mid + 1

    return 0


def count_rotations_generic(nums):
    def condition(mid):
        print("mid: ", mid, "mid number: ", nums[mid])
        if mid > 0 and nums[mid] < nums[mid - 1]:
            return "found"
        elif nums[mid] < nums[-1]:
            return "left"
        else:
            return "right"

    return bs.general_binary_search(0, len(nums) - 1, condition)
