# -*- coding:utf8 -*-


def get_squares(collection: list) -> list:
    """
    Returns squares of elements
    :param collection
    :return:list
    """
    return [item**2 for item in collection]


def get_even_positioned_elements(collection: list) -> list:
    """
    Returns elements from even positions
    :param collection:
    :return:list
    """
    return [item for i, item in enumerate(collection)
            if i % 2 == 0]


def get_cubes_of_evens(collection: list) -> list:
    """
    Returns cubes of even elements from odd positions
    :param collection:
    :return: list
    """
    return [item**3 for i, item in enumerate(collection)
            if i % 2 != 0 and item % 2 == 0]
