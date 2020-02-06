# -*- coding: utf8 -*-

"""
Написать базовый класс `Observable`, который бы позволял наследникам:
при передаче `**kwargs` заносить соответствующие значения как атрибуты.
Сделать так, чтобы при print отображались все публичные атрибуты
"""


class Observable:
    """
    Базовый класс, позволяет наследникам заносить все
    переданные в конструктор именованные значения как
    атрибуты без вызова super().__init__
    """
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.__dict__.update(kwargs)
        return obj

    def __str__(self):
        args = ", ".join(
            ["{0}={1}".format(key, repr(val))
             for key, val in self.__dict__.items()
             if not key.startswith("_")]
        )
        return f"{self.__class__.__name__}({args})"
