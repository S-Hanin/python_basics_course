# -*- coding: utf8 -*-

"""
Напишите итератор `EvenIterator`, который позволяет получить
из списка все элементы, стоящие на чётных индексах.
"""


class EvenIterator:
    """
    Iterates over elements on even positions
    """

    def __init__(self, collection: list):
        self.iterable = collection
        self.current = -2

    def __iter__(self):
        return self

    def __next__(self):
        if not self._has_next():
            raise StopIteration
        return self.iterable[self.current]

    def _has_next(self):
        self.current += 2
        return self.current < len(self.iterable)
