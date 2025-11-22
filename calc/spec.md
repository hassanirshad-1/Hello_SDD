# Calculator Module Specification

This document outlines the complete specification for a basic Python calculator module.

## 1. User Stories

- **As a developer, I want to be able to import a calculator module, so that I can easily perform arithmetic operations in my code.**
- **As a developer, I want to be able to add two numbers together, so that I can get their sum.**
- **As a developer, I want to be able to subtract one number from another, so that I can get their difference.**
- **As a developer, I want to be able to multiply two numbers, so that I can get their product.**
- **As a developer, I want to be able to divide one number by another, so that I can get their quotient.**
- **As a developer, I want to receive a clear error when I try to divide by zero, so that I can handle the exceptional case gracefully.**

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

## 5. Out of Scope

-   **Decimal Precision**: The `decimal` module is not used.
-   **Complex Numbers**: The `complex` type is not supported.
-   **Scientific Functions**: No trigonometry, logarithms, etc.
-   **User Interface**: This is a backend module, not a user-facing application.
-   **Parsing Expressions**: The module does not parse strings like `"2 + 2"`. It only provides direct function calls.
