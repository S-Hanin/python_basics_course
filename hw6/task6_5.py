# -*- coding: utf8 -*-

"""
Написать функцию-генератор `chain`, которая последовательно
итерирует переданные объекты (произвольное количество).
"""
from collections.abc import Sequence


def chain(*args: Sequence):
    """
    Iterates through all collections

    :param args:
    :return: generator
    """
    for collection in args:
        for elem in collection:
            yield elem
