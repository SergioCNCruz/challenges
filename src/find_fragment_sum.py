from typing import List

import pytest


def find_fragment_with_sum(nums: List[int], target_sum: int) -> List[int]:
    """
    Challenge:
        - Find a fragment in a number sequence that sums up to a given target.

    Description:
        - You are given a list of numbers representing a number sequence. Your task is
        to implement a function called `find_fragment_with_sum` that takes the list of
        numbers and a target sum as arguments. The function should return a fragment of
        consecutive numbers in the sequence that adds up to the target sum. If no such
        fragment is found, the function should return an empty list.

    Requirements:
        - Don't change anything except the return value and add you solution bellow the TODO comment.
        - The solution should find a fragment of consecutive numbers in the sequence that
          adds up to the target sum.
        - If a fragment is found, return it as a list of numbers.
        - If no fragment is found, return an empty list.

    Constraints:
        - The input list can contain positive and negative integers.
        - The target sum can be any integer.
        - The fragment should be a contiguous subsequence from the original sequence.

    Hints:
        - You can use two pointers to track the start and end of the fragment.
        - Iterate over the sequence while adjusting the pointers and checking the sum.

    Example:
        - Input:
            nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            target_sum = 15
        - Output:
            [1, 2, 3, 4, 5]
        - Explanation:
            The fragment [1, 2, 3, 4, 5] is a subsequence in the given sequence that adds
            up to the target sum of 15.
    """
    # TODO: Implement your solution below


@pytest.mark.parametrize(
    "nums, target_sum, expected_fragment",
    [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 15, [1, 2, 3, 4, 5]),
        ([4, 6, 8, 10, 12, 14], 30, [8, 10, 12]),
        ([2, 4, 6, 8, 10], 11, []),
        ([1, -2, 3, -4, 5], 2, [1, -2, 3]),
        ([], 5, []),
        ([1, 2, 3, 4, 5], 9, [2, 3, 4]),
        ([10, 20, 30, 40, 50], 100, [10, 20, 30, 40]),
        ([2, 24, 34, 44, 54], 2, [2]),
        ([14, 24, 34, 44, 4], 4, [4]),
    ],
)
def test_find_fragment_with_sum(nums: List[int], target_sum: int, expected_fragment: List[int]):
    fragment = find_fragment_with_sum(nums, target_sum)
    assert fragment == expected_fragment


if __name__ == "__main__":
    pytest.main([__file__])
