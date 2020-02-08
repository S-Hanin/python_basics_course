# -*- coding: utf8 -*-

"""
Написать генератор списка для получения
списка всех публичных атрибутов объекта
"""


def get_public_attributes(obj):
    """
    Get list of public attributes

    :param obj: Any object
    :return: list
    """
    return [attr for attr in dir(obj) if not attr.startswith("_")]
