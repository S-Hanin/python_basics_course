# -*- coding: utf8 -*-

import functools
import operator


def get_odd_number_squares(lower_bound: int, upper_bound: int):
    odd_number_squares = []
    for number in range(lower_bound, upper_bound + 1):
        if number % 2 != 0:
            odd_number_squares.append(number ** 2)
    return odd_number_squares


def print_squares_collection(upper_bound: int):
    collection = get_odd_number_squares(0, upper_bound)
    print(f"odd number squares collections from range 0 .. {upper_bound}")
    print(f"collection size: {len(collection)}")
    print(collection)


def count_numbers_divisible_by(lower_bound: int, upper_bound: int, divider: int):
    return len([number for number in range(lower_bound, upper_bound + 1)
                if number % divider == 0])


def factorial(n: int):
    if n < 0 or not isinstance(n, int):
        raise ValueError(f"Invalid input value. 'n' should be integer > 0")
    return functools.reduce(operator.mul, range(1, n+1), 1)


def get_range(_from: int, _to: int = None, _step: int = 1):
    def _range(_from, _to, _step):
        # условие на случай отрицательного или положительного шага
        condition = (lambda x, y: x < y) if _step > 0 else (lambda x, y: x > y)
        while condition(_from, _to):
            yield _from
            _from += _step

    if _from and _to is None:
        _to = _from
        _from = 0
    if _step == 0:
        raise ValueError("range() arg 3 must not be zero")
    return list(_range(_from, _to, _step))


def prompt_login_password():
    secret_password = "1234"
    while True:
        try:
            login, password = input("Введите логин и пароль: ").split()
            if password == secret_password:
                print(f"Password for user: {login} is correct")
                break
            print(f"Password for user: {login} is incorrect. Please try again")
        except ValueError:
            print("Введите логин и пароль, разделенные пробелом")


if __name__ == '__main__':
    print_squares_collection(5)
