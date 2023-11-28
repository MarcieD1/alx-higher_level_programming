#!/usr/bin/python3

def text_indentation(text):
    """
    Prints the text with 2 new lines after each occurrence of '.', '?', and ':'.

    Args:
        text: A string representing the text.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_marks = ['.', '?', ':']
    lines = text.splitlines()

    for line in lines:
        line = line.strip()  # Remove leading and trailing spaces
        if line:
            for mark in punctuation_marks:
                line = line.replace(mark, mark + '\n\n')
            print(line)


# Example usage
text_indentation("Hello. How are you? I'm fine: Thank you!")
