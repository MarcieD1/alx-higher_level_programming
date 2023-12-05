def read_file(filename=""):
    """Reads a text file (UTF8) and prints its content to stdout.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        None
    """
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            content = file.read()
            print(content, end="")
    except FileNotFoundError:
        pass  # No need to manage file not found exception
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# read_file("example.txt")
