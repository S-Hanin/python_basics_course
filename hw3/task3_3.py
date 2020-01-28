# -*- coding:utf8 -*-


def average(a, b, c, d):
    args = [a, b, c, d]
    max_element = max(args)
    if not hasattr(average, "max") or average.max < max_element:
        average.max = max_element
    return sum(args) / len(args), average.max
