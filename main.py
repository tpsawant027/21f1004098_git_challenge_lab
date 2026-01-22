import sys

import difference
import division
import multiplication
import remainder
import sum as my_sum

USAGE = (
    "Usage: python main.py <operation> <num1> <num2>\n"
    "Available operations: sum, difference, multiplication, division, remainder"
)


def main():
    if len(sys.argv) < 4:
        print(USAGE, file=sys.stderr)
        return 1

    operation = sys.argv[1]

    try:
        num1 = float(sys.argv[2])
        num2 = float(sys.argv[3])
    except ValueError:
        print("Error: Both num1 and num2 must be numbers.", file=sys.stderr)
        return 1

    try:
        match operation:
            case "sum":
                result = my_sum.sum(num1, num2)
            case "difference":
                result = difference.difference(num1, num2)
            case "multiplication":
                result = multiplication.multiplication(num1, num2)
            case "division":
                result = division.division(num1, num2)
            case "remainder":
                result = remainder.remainder(num1, num2)
            case _:
                raise ValueError(f"Unknown operation '{operation}'")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    print(f"{num1} {operation} {num2} = {result}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
