# -*- coding: utf8 -*-

"""
Написать функцию-генератор `cycle` которая бы
возвращала циклический итератор.
"""

from collections.abc import Sequence


def cycle(collection: Sequence):
    """
    Returns `LoopedIterator` instance, who iterates collection
    `repeat` times

    :param collection: sized iterable
    """
    while True:
        yield from (item for item in collection)
