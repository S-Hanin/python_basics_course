# -*- coding: utf8 -*-

"""
Написать декоратор, который будет проверять тип аргументов
при вызове функции согласно аннотации функции.
Декорирование функции без аннотации или с неполной аннотацией
(когда аннотированы не все аргументы) должно рейзить ошибку.
В случае несовпадения переданных во время вызова функции аргументов
с типами аргументов в аннотации - выводить сообщение.
"""
import functools
import logging


class SignatureError(Exception):
    """
    Raise it when function signature have no annotations
    """


def type_check(func):
    """
    Decorator. Checks argument types as had been annotated

    :raises: SignatureError
    """
    if func.__code__.co_argcount != len(func.__annotations__):
        raise SignatureError(f"Не все параметры функции {repr(func)} имеют аннотации")

    @functools.wraps(func)
    def wrap(*args, **kwargs):
        _types = func.__annotations__.values()
        _args = list(args) + list(kwargs.values())

        for arg, proper_type in zip(_args, _types):
            if not isinstance(arg, proper_type):
                logging.warning(f"arg {repr(arg)} is not an "
                                f"instance of expected type {proper_type}")
        return func(*args, **kwargs)

    return wrap


# noinspection Pylint
@type_check
def foo_test(a: int, b: str, c: int):
    print(b)


# noinspection Pylint
@type_check
def bar_test(a: int, b: str, c):
    print(b)


foo_test(1, "first_call", c="2")
foo_test(1, "second call", c=1)
