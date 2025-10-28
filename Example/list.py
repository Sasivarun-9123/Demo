import sys
import math

#!/usr/bin/env python3
"""
Simple prime check utility.

Usage:
    python list.py 17 18 19
    python list.py       # then follow prompt
"""

def is_prime(n: int) -> bool:
        if n <= 1:
                return False
        if n <= 3:
                return True
        if n % 2 == 0 or n % 3 == 0:
                return False
        limit = int(math.isqrt(n))
        i = 5
        while i <= limit:
                if n % i == 0 or n % (i + 2) == 0:
                        return False
                i += 6
        return True

def main(args):
        nums = []
        if args:
                for a in args:
                        try:
                                nums.append(int(a))
                        except ValueError:
                                continue
        else:
                try:
                        nums = [int(x) for x in input("Enter integers separated by spaces: ").split()]
                except Exception:
                        return
        for n in nums:
                print(f"{n}: {'prime' if is_prime(n) else 'not prime'}")

if __name__ == "__main__":
        main(sys.argv[1:])