import sys
from typing import Iterable

#!/usr/bin/env python3
"""
Check whether numbers are even or odd.

Usage:
    - Run without arguments and enter numbers separated by space, or
    - Pass numbers as command-line arguments:
            python set.py 3 4 10
"""


def is_even(n: int) -> bool:
        return n % 2 == 0


def classify_numbers(nums: Iterable[int]) -> Iterable[str]:
        for n in nums:
                yield f"{n} is {'even' if is_even(n) else 'odd'}"


def parse_args(args: Iterable[str]) -> list[int]:
        parsed = []
        for a in args:
                try:
                        parsed.append(int(a))
                except ValueError:
                        # ignore non-integers
                        pass
        return parsed


if __name__ == "__main__":
        args = sys.argv[1:]
        if not args:
                raw = input("Enter integer(s) separated by space: ").strip()
                args = raw.split() if raw else []
        nums = parse_args(args)
        if not nums:
                print("No valid integers provided.")
                sys.exit(1)
        for line in classify_numbers(nums):
                print(line)