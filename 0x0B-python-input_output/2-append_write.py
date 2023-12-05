def append_write(filename="", text=""):
    """Appends a string to the end of a text file (UTF8) and returns the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to be appended to the file.

    Returns:
        int: The number of characters added to the file.
    """
    try:
        with open(filename, mode="a", encoding="utf-8") as file:
            num_characters_added = file.write(text)
            return num_characters_added
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0  # Return 0 if an error occurs

# Example usage:
# characters_added = append_write("example.txt", " Appending text!")
# print(f"Number of characters added: {characters_added}")
