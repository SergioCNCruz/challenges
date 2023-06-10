from typing import List

import pytest


def sort_by_frequency(data: List[int]) -> List[int]:
    """
    Challenge:
        - Sort a list of data by frequency.

    Description:
        - You are given a list of data, and your goal is to sort it in descending order
        based on the frequency of elements. This means that the most frequent elements
        should appear first in the sorted list.

    Requirements:
        - Implement the `sort_by_frequency` function that takes a list of data as a
        parameter.
        - The function should return the list sorted in descending frequency.
        - If there are elements with the same frequency, the original order of those
        elements should be maintained.

    Constraints:
        - The solution should have a time complexity of O(n log n), where n is the number
        of elements in the list.
        - Avoid using external libraries for sorting purposes.

    Hint:
        - Use a dictionary to count the frequency of each element and then sort the list
        based on frequency using the `sorted` function and a lambda function as the
        sorting key.
    """
    # TODO: Add your solution below
    pass


@pytest.mark.parametrize(
    "data, expected_result",
    [
        (
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
        ),  # Test case 1: Unique elements, order remains unchanged
        (
            [10, 20, 10, 30, 20, 10],
            [10, 10, 10, 20, 20, 30],
        ),  # Test case 2: Element 10 appears most frequently, followed by 20 and 30
        (
            ["a", "b", "b", "c", "a"],
            ["a", "a", "b", "b", "c"],
        ),  # Test case 3: Element "a" appears most frequently, followed by "b" and "c"
        (
            [1, 2, 3, 3, 3, 4, 4, 4, 4],
            [4, 4, 4, 4, 3, 3, 3, 2, 1],
        ),  # Test case 4: Element 4 appears most frequently, followed by 3, 2, and 1
        ([], []),  # Test case 5: Empty list
        (
            [100, 200, 300, 400],
            [100, 200, 300, 400],
        ),  # Test case 6: Unique elements, order remains unchanged
        (
            [7, 14, 21, 35, 14, 21],
            [14, 14, 21, 21, 7, 35],
        ),  # Test case 7: Element 14 appears most frequently, followed by 21, 7, and 35
        (
            [1, 1, 1, 2, 2, 2, 3, 3, 3],
            [1, 1, 1, 2, 2, 2, 3, 3, 3],
        ),  # Test case 8: Elements have the same frequency, order remains unchanged
    ],
)
def test_sort_by_frequency(data, expected_result):
    assert sort_by_frequency(data) == expected_result


if __name__ == "__main__":
    pytest.main([__name__])
