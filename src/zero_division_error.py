
# Division error handling example


def divide(dividend, divisor):
    """
    Perform a division and handle division by zero.

    Args:
        dividend (float): Number to be divided.
        divisor (float): Number to divide by.

    Returns:
        None
    """
    try:
        result = dividend / divisor
        print(f"Result: {result}")

    except ZeroDivisionError:
        print("Cannot divide by zero.")


if __name__ == "__main__":
    divide(2, 0)
