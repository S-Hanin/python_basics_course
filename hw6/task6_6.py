# -*- coding: utf8 -*-

"""
You are given two values a and b.
Perform integer division and print a/b.
"""


def divide(a: int, b: int):
    """
    divide a by b
    """
    try:
        a, b = int(a), int(b)
        return a / b
    except ZeroDivisionError as err:
        print(f"Error Code: {err}")
    except ValueError as err:
        print(f"Error Code: {err}")


def main():
    tries = int(input())
    for _ in range(tries):
        a, b = input().split()
        result = divide(a, b)
        if result:
            print(result)


if __name__ == '__main__':
    main()
