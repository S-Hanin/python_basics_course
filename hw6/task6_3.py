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
    val_it = iter(values)

    for key in keys:
        try:
            result[key] = next(val_it)
        except StopIteration:
            result[key] = None
    return result
