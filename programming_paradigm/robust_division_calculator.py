def safe_divide(numerator, denominator):
    """
    Perform division with error handling.

    Args:
        numerator (str or float): The numerator.
        denominator (str or float): The denominator.

    Returns:
        str: Result of division or an error message.
    """
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        denom = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / denom
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
