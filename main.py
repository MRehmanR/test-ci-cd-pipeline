def detect_type(value: str) -> str:
    """Return the data type of the given input value."""
    try:
        int(value)
        return "Integer"
    except ValueError:
        try:
            float(value)
            return "Float"
        except ValueError:
            if value.lower() in ["true", "false"]:
                return "Boolean"
            elif len(value) == 1:
                return "Character"
            else:
                return "String"


if __name__ == "__main__":
    user_input = input("Enter any value: ")
    dtype = detect_type(user_input)
    print(f"The input '{user_input}' is of data type: {dtype}")
