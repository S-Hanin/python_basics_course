# -*- coding:utf8 -*-

# Написать функцию, которая принимает произвольное количество любых аргументов.
#     Аргументами могут быть вложенные списки и кортежи, содержащие числа и другие списки и кортежи.
#     Пример вызова функции: foo(1, 2, [3, 4, (5, 6, 0)], a=(10, 11), b=(3, 4, [5, 6, [7, 8], []]))
#     Функция должна вернуть произведение и сумму всех ненулевых элементов вложенных чисел.
#     Возможны циклические ссылки в аргументах. Пример такого аргумента: a = [1, 2, 3]; a.append(a)
#     При обнаружении циклической ссылки нужно сообщить пользователю и вернуть None.


import functools
import operator


def flatten(iterable):
    def is_cycled_iterable(collection) -> bool:
        return collection in collection

    result = []
    for item in iterable:
        if isinstance(item, (tuple, list)):
            if is_cycled_iterable(item):
                return None
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def add_up_and_multiply(*args, **kwargs):
    flat_list = flatten(list(args) + list(kwargs.values()))
    if not flat_list:
        return None
    _sum = sum(flat_list)
    _mul = functools.reduce(operator.mul, filter(None, flat_list))
    return _sum, _mul
