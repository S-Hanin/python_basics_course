# -*- coding: utf8 -*-

"""
Написать базовый класс `Observable`, который бы позволял наследникам:
при передаче `**kwargs` заносить соответствующие значения как атрибуты.
Сделать так, чтобы при print отображались все публичные атрибуты
"""


class Observable:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        args = ", ".join(
            ["{0}={1}".format(key, repr(val))
             for key, val in self.__dict__.items()
             if not key.startswith("_")]
        )
        return f"{self.__class__.__name__}({args})"
