# -*- coding: utf8 -*-

"""
Написать функцию-генератор `cycle` которая бы
возвращала циклический итератор.
"""

from collections.abc import Sequence


def cycle(collection: Sequence, repeat: int = 1):
    """
    Returns `LoopedIterator` instance, who iterates collection
    `repeat` times

    :param collection: sized iterable
    :param repeat: repeat count
    :return: LoopedIterator
    """

    class LoopedIterator:
        """
        LoopedIterator
        """

        def __init__(self):
            self._current_index = -1
            self._repeat_counter = 0
            self._collection_length = len(collection)

        def __iter__(self):
            return self

        def __next__(self):
            if self._collection_length == 0:
                raise StopIteration
            if not self._has_next():
                self._reset()
            return collection[self._current_index]

        def _has_next(self):
            self._current_index += 1
            return self._current_index < len(collection)

        def _reset(self):
            self._current_index = 0
            self._repeat_counter += 1
            if self._repeat_counter == repeat:
                raise StopIteration

    return LoopedIterator()
