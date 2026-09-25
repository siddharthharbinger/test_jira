"""Reproduction script for ZeroDivisionError in calculate_ratio."""
import sys
from calculation import calculate_ratio

if __name__ == "__main__":
    try:
        res = calculate_ratio(10.0, 0.0)
        if res == 0.0:
            print("PASS: calculate_ratio(10.0, 0.0) returned 0.0")
            sys.exit(0)
        else:
            sys.stderr.write(f"FAIL: Expected 0.0, got {res}\n")
            sys.exit(1)
    except ZeroDivisionError as err:
        sys.stderr.write(f"REPRODUCED ZeroDivisionError: {err}\n")
        sys.exit(1)
