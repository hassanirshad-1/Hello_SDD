# Calculator Module Specification

This document outlines the complete specification for a basic Python calculator module.

## 1. User Stories

- **As a developer, I want to be able to import a calculator module, so that I can easily perform arithmetic operations in my code.**
- **As a developer, I want to be able to add two numbers together, so that I can get their sum.**
- **As a developer, I want to be able to subtract one number from another, so that I can get their difference.**
- **As a developer, I want to be able to multiply two numbers, so that I can get their product.**
- **As a developer, I want to be able to divide one number by another, so that I can get their quotient.**
- **As a developer, I want to receive a clear error when I try to divide by zero, so that I can handle the exceptional case gracefully.**
- **As a developer, I want to be able to raise a number to a given power, so that I can perform exponentiation operations for calculations involving growth, decay, or geometric progressions.**

## 2. Function Signatures (Python 3.12+)

```python
def add(a: int | float, b: int | float) -> int | float:
    ...

def subtract(a: int | float, b: int | float) -> int | float:
    ...

def multiply(a: int | float, b: int | float) -> int | float:
    ...

def divide(a: int | float, b: int | float) -> float:
    ...

def power(base: int | float, exponent: int | float) -> int | float:
    ...
```

## 3. Acceptance Criteria

### Addition

- **GIVEN** `a = 5` and `b = 10`
- **WHEN** I call `add(a, b)`
- **THEN** the result is `15`

- **GIVEN** `a = 3.14` and `b = 2.71`
- **WHEN** I call `add(a, b)`
- **THEN** the result is `5.85`

- **GIVEN** `a = 10` (integer) and `b = 5.5` (float)
- **WHEN** I call `add(a, b)`
- **THEN** the result is `15.5` (float)

- **GIVEN** `a = "hello"` and `b = 5`
- **WHEN** I call `add(a, b)`
- **THEN** a `TypeError` is raised

### Subtraction

- **GIVEN** `a = 10` and `b = 5`
- **WHEN** I call `subtract(a, b)`
- **THEN** the result is `5`

- **GIVEN** `a = 5` and `b = 10`
- **WHEN** I call `subtract(a, b)`
- **THEN** the result is `-5`

- **GIVEN** `a = 10` (integer) and `b = 2.5` (float)
- **WHEN** I call `subtract(a, b)`
- **THEN** the result is `7.5` (float)

- **GIVEN** `a = 10` and `b = "world"`
- **WHEN** I call `subtract(a, b)`
- **THEN** a `TypeError` is raised

### Multiplication

- **GIVEN** `a = 6` and `b = 7`
- **WHEN** I call `multiply(a, b)`
- **THEN** the result is `42`

- **GIVEN** `a = 100` and `b = 0`
- **WHEN** I call `multiply(a, b)`
- **THEN** the result is `0`

- **GIVEN** `a = -5` and `b = -5`
- **WHEN** I call `multiply(a, b)`
- **THEN** the result is `25`

- **GIVEN** `a = "foo"` and `b = "bar"`
- **WHEN** I call `multiply(a, b)`
- **THEN** a `TypeError` is raised

### Division

- **GIVEN** `a = 20` and `b = 5`
- **WHEN** I call `divide(a, b)`
- **THEN** the result is `4.0`

- **GIVEN** `a = 10` and `b = 0`
- **WHEN** I call `divide(a, b)`
- **THEN** a `ValueError` is raised with the message "Cannot divide by zero"

- **GIVEN** `a = 10` and `b = "zero"`
- **WHEN** I call `divide(a, b)`
- **THEN** a `TypeError` is raised

### Power

**Happy Path Scenarios:**

- **GIVEN** `base = 2` and `exponent = 10`
- **WHEN** I call `power(base, exponent)`
- **THEN** the result is `1024`

- **GIVEN** `base = 9.0` and `exponent = 0.5`
- **WHEN** I call `power(base, exponent)`
- **THEN** the result is `3.0`

**Edge Cases:**

- **GIVEN** `base = 100` and `exponent = 0`
- **WHEN** I call `power(base, exponent)`
- **THEN** the result is `1`

- **GIVEN** `base = 0` and `exponent = 0`
- **WHEN** I call `power(base, exponent)`
- **THEN** the result is `1`

- **GIVEN** `base = -5` and `exponent = 2` (even integer)
- **WHEN** I call `power(base, exponent)`
- **THEN** the result is `25`

- **GIVEN** `base = -5` and `exponent = 3` (odd integer)
- **WHEN** I call `power(base, exponent)`
- **THEN** the result is `-125`

- **GIVEN** `base = 2` and `exponent = -2`
- **WHEN** I call `power(base, exponent)`
- **THEN** the result is `0.25`

**Error Cases:**

- **GIVEN** `base = 0` and `exponent = -1`
- **WHEN** I call `power(base, exponent)`
- **THEN** a `ZeroDivisionError` is raised with a message like "0.0 cannot be raised to a negative power"

- **GIVEN** `base = -4` and `exponent = 0.5` (negative base, fractional exponent)
- **WHEN** I call `power(base, exponent)`
- **THEN** a `ValueError` is raised with a message like "Negative number cannot be raised to a fractional power"

- **GIVEN** `base = "hello"` and `exponent = 2`
- **WHEN** I call `power(base, exponent)`
- **THEN** a `TypeError` is raised

## 4. Design and Edge Case Analysis

1.  **Floating-Point Precision**:
    - **Behavior**: The calculator will use standard IEEE 754 floating-point arithmetic. `0.1 + 0.2` will result in `0.30000000000000004`.
    - **Reasoning**: This is the idiomatic and performant standard in Python.

2.  **Division by Zero**:
    - **Behavior**: Attempting to divide by zero will raise a `ValueError` with the message: `"Cannot divide by zero"`.
    - **Reasoning**: This "fail-fast" approach prevents silent error propagation and forces explicit exception handling.

3.  **Type Preservation Rules**:
    - **Behavior**:
        - Any operation with a `float` results in a `float`.
        - Division (`/`) always results in a `float`.
        - `int` operations (`+`, `-`, `*`) on two `int`s result in an `int`.
    - **Reasoning**: Prevents data loss and aligns with Python 3's standard numeric behavior.

4.  **Zero Behavior**:
    - **Behavior**: Zero acts as the additive identity (`x + 0 = x`), the absorbing element for multiplication (`x * 0 = 0`), and `0 / x = 0.0` for non-zero `x`.
    - **Reasoning**: Follows fundamental mathematical axioms for predictable behavior.

5.  **Negative Number Handling**:
    - **Behavior**: Standard arithmetic rules apply. No special logic is implemented.
    - **Reasoning**: Python's built-in operators handle negative numbers correctly.

6.  **Very Large Number Limits**:
    - **Behavior**: `int` types have arbitrary precision, limited by system memory. `float` types are 64-bit and will overflow to `inf` beyond ~1.8e308.
    - **Reasoning**: Inherits Python's powerful and standard numeric type capabilities.

7.  **Power Function (`power`)**:
    - **User Story**: The primary goal is to provide a standard exponentiation function for developers.
    - **Exponent Type**: The `exponent` can be an `int` or a `float` to support both integer powers and roots (e.g., `x**0.5`).
    - **`power(x, 0)`**: Any number `x` raised to the power of `0` is `1`. This is a standard mathematical identity.
    - **`power(0, 0)`**: Following Python's convention, `0**0` will be defined as `1`. While mathematically ambiguous, this is the most practical definition for programming contexts.
    - **Negative Base with Fractional Exponent**: Operations like `(-4)**0.5` result in a complex number (`2j`). Since our calculator is scoped to `int` and `float` types (as per the "Out of Scope" section), attempting this will raise a `ValueError` to prevent returning a complex number.
    - **Large Results**: The function will handle very large results by leveraging Python's arbitrary-precision integers (e.g., `2**1000`). For floating-point results, it will adhere to standard overflow behavior, resulting in `float('inf')` if the number exceeds the 64-bit float limit.
    - **Error Handling**:
        - A `ValueError` is raised for mathematical domain errors (negative base to a fractional power).
        - A `ZeroDivisionError` is raised for `0` raised to a negative power, as this is equivalent to division by zero.
        - A `TypeError` is raised for non-numeric inputs.

## 5. Out of Scope

-   **Decimal Precision**: The `decimal` module is not used.
-   **Complex Numbers**: The `complex` type is not supported.
-   **Scientific Functions**: No trigonometry, logarithms, etc.
-   **User Interface**: This is a backend module, not a user-facing application.
-   **Parsing Expressions**: The module does not parse strings like `"2 + 2"`. It only provides direct function calls.
