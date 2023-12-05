#!/usr/bin/python3
def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of characters written.

    Args:
        filename (str): The name of the file to write.
        text (str): The string to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """
    try:
        with open(filename, mode="w", encoding="utf-8") as file:
            num_characters_written = file.write(text)
            return num_characters_written
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0  # Return 0 if an error occurs

# Example usage:
# characters_written = write_file("example.txt", "Hello, World!")
# print(f"Number of characters written: {characters_written}")
