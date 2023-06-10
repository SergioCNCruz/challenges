import pytest


def compress_text(text: str) -> str:
    """
    Challenge:
        - Compress a text by removing consecutive repeated characters.

    Description:
        - You are given a string of text. Your task is to compress the text by removing consecutive repeated characters.
        - The compression is done by replacing the repeated characters with their count.

    Requirements:
        - Implement a function called `compress_text` that takes a string as input and returns a compressed version of the text.
        - The function should remove consecutive repeated characters and replace them with their count.

    Constraints:
        - The input text can contain both uppercase and lowercase alphabets.
        - The input text can also contain special characters and spaces.

    Hints:
        - You can iterate over the string and compare each character with the next one to identify repetitions.
    """
    # TODO: Add your solution bellow
    pass


@pytest.mark.parametrize(
    "text, expected_result",
    [
        (
            "aabbbcccc",
            "a2b3c4",
        ),  # Test Case 1: Repeated characters "a", "b", and "c" are compressed.
        (
            "abc",
            "abc",
        ),  # Test Case 2: No consecutive repeated characters, the text remains unchanged.
        (
            "aaabbbccc",
            "a3b3c3",
        ),  # Test Case 3: Repeated characters "a", "b", and "c" are compressed.
        ("", ""),  # Test Case 4: Empty text, the compressed version is also empty.
        (
            "abbcccdd",
            "ab2c3d2",
        ),  # Test Case 5: Repeated characters "b", "c", and "d" are compressed.
        (
            "xxxyyyyyzzzzzz",
            "x3y5z6",
        ),  # Test Case 6: Repeated characters "x", "y", and "z" are compressed.
        (
            "abcdefg",
            "abcdefg",
        ),  # Test Case 7: No consecutive repeated characters, the text remains unchanged.
    ],
)
def test_compress_text(text, expected_result):
    compressed_text = compress_text(text)
    assert compressed_text == expected_result


if __name__ == "__main__":
    pytest.main([__file__])
