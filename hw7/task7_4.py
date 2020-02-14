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

    # raises SignatureError at launch time
    if func.__code__.co_argcount != len(func.__annotations__):
        raise SignatureError(f"Not all {func} arguments "
                             f"has type annotation")

    @functools.wraps(func)
    def wrap(*args, **kwargs):
        _types = func.__annotations__.items()
        _args = list(args) + list(kwargs.values())

        for arg, annotation in zip(_args, _types):
            arg_name, arg_type = annotation
            if not isinstance(arg, arg_type):
                logging.warning(f"argument {arg_name}={repr(arg)} is not an "
                                f"instance of expected type {arg_type} "
                                f"in {func}\n"
                                f"file: {wrap.__code__.co_filename} "
                                f"line: {func.__code__.co_firstlineno}")
        return func(*args, **kwargs)

    return wrap


# noinspection Pylint
@type_check
def foo_test(a: int, b: str, c: int):
    print(b)


# noinspection Pylint
# @type_check
def bar_test(a: int, b: str, c):
    print(b)


foo_test(1, "first_call", c="2")
foo_test(1, "second call", c=1)
