
import pytest
from calc import calculator

# Test cases for the add function
def test_add_integers():
    assert calculator.add(2, 3) == 5

def test_add_floats():
    assert calculator.add(2.5, 3.5) == 6.0

def test_add_mixed_types():
    assert calculator.add(2, 3.5) == 5.5

def test_add_with_negative():
    assert calculator.add(5, -2) == 3

def test_add_with_zero():
    assert calculator.add(5, 0) == 5

def test_add_invalid_type():
    with pytest.raises(TypeError):
        calculator.add("a", 2)

# Test cases for the subtract function
def test_subtract_integers():
    assert calculator.subtract(5, 3) == 2

def test_subtract_floats():
    assert calculator.subtract(5.5, 3.2) == 2.3

def test_subtract_mixed_types():
    assert calculator.subtract(5, 3.5) == 1.5

def test_subtract_with_negative():
    assert calculator.subtract(5, -2) == 7

def test_subtract_larger_from_smaller():
    assert calculator.subtract(3, 5) == -2

def test_subtract_with_zero():
    assert calculator.subtract(5, 0) == 5

def test_subtract_invalid_type():
    with pytest.raises(TypeError):
        calculator.subtract("a", 2)

# Test cases for the multiply function
def test_multiply_integers():
    assert calculator.multiply(2, 3) == 6

def test_multiply_floats():
    assert calculator.multiply(2.5, 3.0) == 7.5

def test_multiply_mixed_types():
    assert calculator.multiply(2, 3.5) == 7.0

def test_multiply_with_negative():
    assert calculator.multiply(5, -2) == -10

def test_multiply_two_negatives():
    assert calculator.multiply(-5, -2) == 10

def test_multiply_by_zero():
    assert calculator.multiply(5, 0) == 0

def test_multiply_invalid_type():
    with pytest.raises(TypeError):
        calculator.multiply("a", 2)

# Test cases for the divide function
def test_divide_integers():
    assert calculator.divide(6, 3) == 2.0

def test_divide_floats():
    assert calculator.divide(7.5, 2.5) == 3.0

def test_divide_mixed_types():
    assert calculator.divide(7, 3.5) == 2.0

def test_divide_with_negative():
    assert calculator.divide(10, -2) == -5.0

def test_divide_two_negatives():
    assert calculator.divide(-10, -2) == 5.0

def test_divide_zero_by_number():
    assert calculator.divide(0, 5) == 0.0

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(5, 0)

def test_divide_invalid_type():
    with pytest.raises(TypeError):
        calculator.divide("a", 2)
