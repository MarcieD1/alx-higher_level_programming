#!/usr/bin/python3
if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    args = sys.argv[1:]  # Exclude the script name from the arguments
    result = sum(int(arg) for arg in args)

    print(result)
