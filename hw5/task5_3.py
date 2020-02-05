# -*- coding: utf8 -*-

"""
Написать базовый класс `Observable`, который бы позволял наследникам:
при передаче `**kwargs` заносить соответствующие значения как атрибуты.
Сделать так, чтобы при print отображались все публичные атрибуты
"""

import pprint


class Observable:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        args = ", ".join([f"{item[0]}={item[1]}" for item in self.__dict__.items()])
        return f"{self.__class__.__name__}({args})"


a = Observable(a=1, b=2, c="hello")
print(a)