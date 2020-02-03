# -*- coding:utf8 -*-

# Написать функцию, которая принимает произвольное количество любых аргументов.
#     Аргументами могут быть вложенные списки и кортежи, содержащие числа и другие списки и кортежи.
#     Пример вызова функции: foo(1, 2, [3, 4, (5, 6, 0)], a=(10, 11), b=(3, 4, [5, 6, [7, 8], []]))
#     Функция должна вернуть произведение и сумму всех ненулевых элементов вложенных чисел.
#     Возможны циклические ссылки в аргументах. Пример такого аргумента: a = [1, 2, 3]; a.append(a)
#     При обнаружении циклической ссылки нужно сообщить пользователю и вернуть None.


import functools
import operator


def is_cycled_iterable(collection) -> bool:
    collections = [collection]
    visited = []
    while len(collections) > 0:
        visited.append(collections.pop())
        for item in visited[-1]:
            if item in visited:
                return True
            if isinstance(item, (list, tuple)):
                collections.append(item)
    return False


def flatten(iterable):
    result = []
    for item in iterable:
        if isinstance(item, (tuple, list)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def add_up_and_multiply(*args, **kwargs):
    arguments = list(args) + list(kwargs.values())
    if is_cycled_iterable(arguments):
        print("arguments has cycled links")
        return None
    flat_list = flatten(arguments)
    _sum = sum(flat_list)
    _mul = functools.reduce(operator.mul, filter(None, flat_list))
    return _sum, _mul
