# -*- coding: utf8 -*-

"""
Есть два списка разной длины, в одном ключи, в другом значения.
Составить словарь. Для ключей, для которых нет значений использовать
`None` в качестве значения. Значения, для которых нет ключей игнорировать.
"""


def associate(keys, values):
    """
    Associates keys with values. Drops value if key is absent.
    None associates with key if value is absent.

    :param keys:
    :param values:
    :return: dict
    """
    result = {}
    key_it, val_it = iter(keys), iter(values)

    while True:
        try:
            key = next(key_it)
        except StopIteration:
            break

        try:
            val = next(val_it)
        except StopIteration:
            val = None
        result[key] = val

    return result
