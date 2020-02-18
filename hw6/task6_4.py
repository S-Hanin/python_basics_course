# -*- coding: utf8 -*-

"""
Написать функцию-генератор `cycle` которая бы
возвращала циклический итератор.
"""

from collections.abc import Sequence


def cycle(collection: Sequence):
    """
    Iterate elements of collection infinitely

    :param collection: sized iterable
    """
    while True:
        yield from (item for item in collection)
