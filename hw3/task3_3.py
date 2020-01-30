# -*- coding:utf8 -*-

# Написать функцию, которая будет принимать
# только 4 позиционных аргументы (все аргументы числовые).
# Функция должна вернуть среднее арифметическое
# аргументов и самый большой аргумент за все время вызовов этой функции.
# Пример: foo(1,2,3,4) -> 2.5, 4
#         foo(-3, -2, 10, 1) -> 1.5, 10
#         foo(7,8,8,1) -> 6, 10


def average(a, b, c, d) -> tuple:
    args = [a, b, c, d]
    max_element = max(args)
    if not hasattr(average, "max") or average.max < max_element:
        average.max = max_element
    return sum(args) / len(args), average.max
