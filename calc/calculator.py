"""
A basic calculator module providing arithmetic operations.
"""

def add(a: int | float, b: int | float) -> int | float:
    """
    Adds two numbers and returns their sum.

    Args:
        a (int | float): The first number.
        b (int | float): The second number.

    Returns:
        int | float: The sum of a and b. The return type is float if either input is a float,
                     otherwise it is an int.

    Raises:
        TypeError: If a or b are not of type int or float.

    Examples:
        >>> add(5, 10)
        15
        >>> add(3.14, 2.71)
        5.85
        >>> add(10, 5.5)
        15.5
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be integers or floats.")
    return a + b

def subtract(a: int | float, b: int | float) -> int | float:
    """
    Subtracts the second number from the first and returns the difference.

    Args:
        a (int | float): The first number (minuend).
        b (int | float): The second number (subtrahend).

    Returns:
        int | float: The difference of a and b. The return type is float if either input is a float,
                     otherwise it is an int.

    Raises:
        TypeError: If a or b are not of type int or float.

    Examples:
        >>> subtract(10, 5)
        5
        >>> subtract(5, 10)
        -5
        >>> subtract(10, 2.5)
        7.5
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be integers or floats.")
    return a - b

def multiply(a: int | float, b: int | float) -> int | float:
    """
    Multiplies two numbers and returns their product.

    Args:
        a (int | float): The first number.
        b (int | float): The second number.

    Returns:
        int | float: The product of a and b. The return type is float if either input is a float,
                     otherwise it is an int.

    Raises:
        TypeError: If a or b are not of type int or float.

    Examples:
        >>> multiply(6, 7)
        42
        >>> multiply(100, 0)
        0
        >>> multiply(-5, -5)
        25
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be integers or floats.")
    return a * b

def divide(a: int | float, b: int | float) -> float:
    """
    Divides the first number by the second and returns the quotient.

    Args:
        a (int | float): The numerator.
        b (int | float): The denominator.

    Returns:
        float: The quotient of a divided by b. Always returns a float.

    Raises:
        ValueError: If the denominator b is zero.
        TypeError: If a or b are not of type int or float.

    Examples:
        >>> divide(20, 5)
        4.0
        >>> divide(10, 0)
        Traceback (most recent call last):
            ...
        ValueError: Cannot divide by zero
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be integers or floats.")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
