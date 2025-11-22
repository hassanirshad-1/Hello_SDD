
import argparse
from calc import calculator

def main():
    """Command-line interface for the calculator module."""
    parser = argparse.ArgumentParser(
        description="A simple command-line calculator.",
        epilog="Example: python calc_cli.py add 5 3"
    )

    parser.add_argument(
        "operation",
        choices=["add", "subtract", "multiply", "divide", "power"],
        help="The operation to perform."
    )
    parser.add_argument(
        "numbers",
        type=float,
        nargs=2,
        help="The two numbers to operate on."
    )

    args = parser.parse_args()

    operation = args.operation
    num1, num2 = args.numbers

    try:
        if operation == "add":
            result = calculator.add(num1, num2)
        elif operation == "subtract":
            result = calculator.subtract(num1, num2)
        elif operation == "multiply":
            result = calculator.multiply(num1, num2)
        elif operation == "divide":
            result = calculator.divide(num1, num2)
        elif operation == "power":
            result = calculator.power(num1, num2)

        print(f"Result: {result}")

    except (ValueError, TypeError, ZeroDivisionError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
