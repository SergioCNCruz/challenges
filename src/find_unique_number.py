from typing import List

import pytest


def find_unique_number(numbers: List) -> int:
    """
    Challenge:
        - Find the number that appears only once in a list of repeated numbers.

    Description:
        - You are given a list of integers, where all numbers are repeated except for one.
        - Your goal is to find and return the number that appears only once in the list.

    Requirements:
        - Implement the function find_unique_number, which takes a list of integers as a
        parameter and returns the unique number that appears only once in the list.
        - The unique number will always be present in the list.
        - The list will always have an odd number of elements.

    Constraints:
        - The solution should have a time complexity of O(n) and space complexity of O(1),
        where n is the number of elements in the list.
        - Avoid using external libraries.

    Hint:
    - Consider using the XOR (^) operator to efficiently solve this problem.
    """
    # TODO: Add your solution bellow
    result = 0
    for number in numbers:
        result ^= number
    return result


@pytest.mark.parametrize(
    "numbers, expected",
    [
        (
            [5, 2, 2, 1, 1, 4, 4],
            5,
        ),  # Test case 1: Unique number at the beginning of the list
        ([2, 2, 1, 1, 4, 4, 3], 3),  # Test case 2: Unique number at the end of the list
        (
            [2, 2, 1, 1, 3, 4, 4],
            3,
        ),  # Test case 3: Unique number in the middle of the list
        ([-1, -1, -2, -2, -3], -3),  # Test case 4: Negative numbers
        ([-1, -1, 2, 2, -3, 4, 4], -3),  # Test case 5: Positive and negative numbers
        ([42], 42),  # Test case 6: List with a single element
        ([7, 7, 7], 7),  # Test case 7: List with three repeated elements
        ([8, 8, 8, 8, 8], 8),  # Test case 8: List with five repeated elements
        (
            [1000, 1000, 10000, 10000, 999, 999, 5000],
            5000,
        ),  # Test case 9: List with larger numbers
        (
            [-10, -10, -100, -100, -5, -5, -200],
            -200,
        ),  # Test case 10: List with smaller numbers
    ],
)
def test_find_unique_number(numbers, expected):
    assert find_unique_number(numbers) == expected


if __name__ == "__main__":
    pytest.main([__file__])
