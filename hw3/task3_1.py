# -*- coding:utf8 -*-

# Написать несколько функций, которые в качестве единственного аргумента принимают список (или кортеж) целых чисел.
#      - первая функция должна вернуть квадраты элементов коллекции;
#      - вторая функция должна вернуть только элементы на четных позициях (upd: счет элементов начинается с единицы);
#      - третья функция возвращает кубы четных элементов на нечетных позициях


def get_squares(collection: list) -> list:
    """
    Returns squares of elements

    :param collection: numbers collection
    :return:list
    """
    return [item ** 2 for item in collection]


def get_even_positioned_elements(collection: list) -> list:
    """
    Returns elements from even positions

    :param collection: numbers collection
    :return:list
    """
    return collection[::2]


def get_cubes_of_evens_on_odd_places(collection: list) -> list:
    """
    Returns cubes of even elements from odd positions

    :param collection: numbers collection
    :return: list
    """
    return [item ** 3 for item in collection[1::2]
            if item % 2 == 0]
