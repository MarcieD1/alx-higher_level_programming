def class_to_json(obj):
    """Returns a dictionary description for JSON serialization of an object.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary describing the serializable attributes of the object.
    """
    serializable_attributes = {}

    # Iterate through all attributes of the object
    for attr_name, attr_value in obj.__dict__.items():
        if _is_serializable(attr_value):
            serializable_attributes[attr_name] = attr_value

    return serializable_attributes


def _is_serializable(value):
    """Checks if a value is serializable (list, dict, str, int, bool)."""
    return isinstance(value, (list, dict, str, int, bool))


# Example usage:
if __name__ == "__main__":
    # Your class definition here (either 8-my_class or 8-my_class_2)

    # Example with 8-my_class
    m = MyClass("John")
    m.number = 89
    print(type(m))
    print(m)

    mj = class_to_json(m)
    print(type(mj))
    print(mj)

    # Example with 8-my_class_2
    m2 = MyClass("John")
    m2.win()
    print(type(m2))
    print(m2)

    mj2 = class_to_json(m2)
    print(type(mj2))
    print(mj2)
