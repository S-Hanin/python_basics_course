# -*- coding: utf8 -*-

"""
Преобразовать вызов функции с конечным количеством
позиционных аргументов f(a, b, c, d) в вызов
вида f(a)(b)(c)(d), используя декоратор.
"""


def carry(func):
    """
    Carrying decorator.
    """
    args = []

    def wrap(arg):
        args.append(arg)
        if len(args) == func.__code__.co_argcount:
            return func(*args)
        return wrap

    return wrap


# noinspection Pylint
@carry
def foo_2_test(a, b):
    return a + b


# noinspection Pylint
@carry
def foo_3_test(a, b, c):
    return a + b + c


if __name__ == '__main__':
    # noinspection Pylint
    print(foo_2_test(1)(2))
    # noinspection Pylint
    print(foo_3_test(1)(2)(3))
