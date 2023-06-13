from typing import List

import pytest


def get_fragments(lst: List[int]) -> List:
    """
    Challenge:
        - Return the items of a list in increasing fragments.

    Description:
        1. Create a list with at least 10 items of your choice.
        2. Implement a function called `get_fragments` that takes the list as an argument.
        3. The `get_fragments` function should return a list containing the fragments of
        the original list in ascending order.
           - In the first fragment, include only the first item.
           - In the second fragment, include the first and second items.
           - In the third fragment, include the first, second, and third items.
           - Continue this pattern until all items in the list are included.
        4. Test your function by passing different lists as arguments and
        verify if the fragments are returned correctly.

    Requirements:
        - Python 3.6 or above

    Constraints:
    - The input list must have at least one element.

    Hints:
    - You can use list slicing to extract the fragments from the input list.

    """
    # TODO: Add your solution below
    return [lst[: idx + 1] for idx in range(len(lst))]


@pytest.mark.parametrize(
    "test_list, expected_result",
    [
        (
            [1, 2, 3, 4, 5],
            [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]],
        ),  # Test case 1: Increasing numbers
        (
            ["a", "b", "c"],
            [["a"], ["a", "b"], ["a", "b", "c"]],
        ),  # Test case 2: Increasing letters
        (
            [10, 20, 30, 40, 50, 60],
            [
                [10],
                [10, 20],
                [10, 20, 30],
                [10, 20, 30, 40],
                [10, 20, 30, 40, 50],
                [10, 20, 30, 40, 50, 60],
            ],
        ),  # Test case 3: Increasing numbers
        (
            ["apple", "banana", "cherry", "date"],
            [
                ["apple"],
                ["apple", "banana"],
                ["apple", "banana", "cherry"],
                ["apple", "banana", "cherry", "date"],
            ],
        ),  # Test case 4: Increasing fruits
        ([True, False], [[True], [True, False]]),  # Test case 5: Increasing booleans
        (
            [7, 14, 21, 28],
            [[7], [7, 14], [7, 14, 21], [7, 14, 21, 28]],
        ),  # Test case 6: Increasing multiples of 7
        (
            ["red", "green", "blue", "yellow"],
            [
                ["red"],
                ["red", "green"],
                ["red", "green", "blue"],
                ["red", "green", "blue", "yellow"],
            ],
        ),  # Test case 7: Increasing colors
        (
            [0.5, 1.5, 2.5, 3.5, 4.5],
            [
                [0.5],
                [0.5, 1.5],
                [0.5, 1.5, 2.5],
                [0.5, 1.5, 2.5, 3.5],
                [0.5, 1.5, 2.5, 3.5, 4.5],
            ],
        ),  # Test case 8: Increasing floating-point numbers
        (
            ["one", "two", "three", "four", "five", "six"],
            [
                ["one"],
                ["one", "two"],
                ["one", "two", "three"],
                ["one", "two", "three", "four"],
                ["one", "two", "three", "four", "five"],
                ["one", "two", "three", "four", "five", "six"],
            ],
        ),  # Test case 9: Increasing words
        (
            [100, 200, 300, 400],
            [[100], [100, 200], [100, 200, 300], [100, 200, 300, 400]],
        ),  # Test case 10: Increasing numbers
    ],
)
def test_get_fragments(test_list, expected_result):
    fragments = get_fragments(test_list)
    assert fragments == expected_result


if __name__ == "__main__":
    pytest.main([__file__])
