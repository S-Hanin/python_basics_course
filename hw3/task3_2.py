# -*- coding:utf8 -*-

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
