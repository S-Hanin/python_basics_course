# -*- coding:utf8 -*-

# Написать функцию, которая принимает произвольное количество любых аргументов.
#     Аргументами могут быть вложенные списки и кортежи, содержащие числа и другие списки и кортежи.
#     Пример вызова функции: foo(1, 2, [3, 4, (5, 6, 0)], a=(10, 11), b=(3, 4, [5, 6, [7, 8], []]))
#     Функция должна вернуть произведение и сумму всех ненулевых элементов вложенных чисел.
#     Возможны циклические ссылки в аргументах. Пример такого аргумента: a = [1, 2, 3]; a.append(a)
#     При обнаружении циклической ссылки нужно сообщить пользователю и вернуть None.


import functools
import operator
from collections.abc import Iterable


def is_cycled_iterable(collection) -> bool:
    """
    Checks that collection has cycled links at arbitrary level

    :param collection:
    :return: bool
    """
    collections = [collection]
    visited = {}
    while len(collections) > 0:
        current = collections.pop()
        visited[id(current)] = True
        for item in current:
            if visited.get(id(item), False):
                return True
            if isinstance(item, Iterable):
                collections.append(item)
    return False


def flatten(iterable) -> list:
    """
    Unwrap arbitrary nesting iterable

    :param iterable: any iterable
    :return: iterable
    """
    result = []
    for item in iterable:
        if isinstance(item, Iterable):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def add_up_and_multiply(*args, **kwargs) -> (int, int):
    """
    Accept any number of positional and keyword arguments
    and return their sum and product.
    Parameters can be any number or iterable of numbers

    :param args: number or iterable of numbers
    :param kwargs: number or iterable of numbers
    :return: tuple(int, int)
    """
    arguments = list(args) + list(kwargs.values())
    if is_cycled_iterable(arguments):
        print("arguments has cycled links")
        return None
    flat_list = flatten(arguments)
    _sum = sum(flat_list)
    _mul = functools.reduce(operator.mul, filter(None, flat_list))
    return _sum, _mul
