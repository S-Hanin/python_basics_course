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
import inspect
import logging


class SignatureError(Exception):
    """
    Raise it when function signature have no annotations
    """


def _replace_none_in_annotation(parameter):
    """
    Does replacing in such annotations as (int, None) to (int, NoneType)
    """
    if isinstance(parameter.annotation, tuple) and None in parameter.annotation:
        annotation = tuple(item if item is not None else type(item)
                           for item in parameter.annotation)
        return parameter.replace(annotation=tuple(annotation))
    return parameter


def _inspect_var_positional(arg_name, arg_value, parameter, func):
    """
    Does inspection of *args parameters
    """
    if parameter.kind == parameter.VAR_POSITIONAL:
        if not all(isinstance(item, parameter.annotation) for item in arg_value):
            return True


def _inspect_var_keyword(arg_name, arg_value, parameter, func):
    """
    Does inspection of **kwargs parameters
    """
    if parameter.kind == parameter.VAR_KEYWORD:
        if not all(isinstance(item, parameter.annotation) for item in arg_value.values()):
            return True


def _inspect_common_parameter(arg_name, arg_value, parameter, func):
    """
    Does inspection of positional and named parameters
    """
    if parameter.kind in (parameter.POSITIONAL_ONLY, parameter.POSITIONAL_OR_KEYWORD,
                          parameter.KEYWORD_ONLY):
        if not isinstance(arg_value, parameter.annotation):
            return True


def type_check(func):
    """
    Decorator. Checks argument types as had been annotated
    checks signatures such:
        foo(a: int)
        foo(a: (int, None))
        foo(*args, **kwargs)

    :raises: SignatureError
    """

    # check return type
    sig = inspect.signature(func)
    if sig.return_annotation is sig.empty:
        raise SignatureError(f"{func} has not return type annotation")

    # check parameters have annotations
    param_without_annotation = [arg_name for arg_name, param in sig.parameters.items()
                                if param.annotation is sig.empty]
    if len(param_without_annotation) > 0:
        raise SignatureError(f"{func} arguments {param_without_annotation}"
                             f" has not type annotation")

    @functools.wraps(func)
    def wrap(*args, **kwargs):
        ba = sig.bind(*args, **kwargs)

        for param_signature, argument in zip(sig.parameters.items(), ba.arguments.items()):
            arg_name, arg_value = argument
            _, parameter = param_signature

            parameter = _replace_none_in_annotation(parameter)

            checks = [_inspect_var_positional(arg_name, arg_value, parameter, func),
                      _inspect_var_keyword(arg_name, arg_value, parameter, func),
                      _inspect_common_parameter(arg_name, arg_value, parameter, func)]
            if any(checks):
                logging.warning(f"argument {arg_name}={repr(arg_value)} is not an "
                                f"instance of expected type {parameter.annotation} "
                                f"in {func}\n"
                                f"file: {func.__code__.co_filename} "
                                f"line: {func.__code__.co_firstlineno}")
        return func(*args, **kwargs)

    return wrap


if __name__ == '__main__':
    @type_check
    def a_test(*args: int, k: str) -> None:
        pass


    @type_check
    def b_test(a: (int, None), **kwargs: str) -> None:
        pass


    @type_check
    def c_test(a: int, b: str, c: int) -> None:
        pass


    # @type_check
    def d_test(a: int, b: str, c) -> None:  # raises signature error
        pass


    a_test(1, 2, '3', k="hello")
    b_test(None, b="a", c=1)
    c_test(1, "first_call", c="2")
    c_test(1, "second call", c=1)
