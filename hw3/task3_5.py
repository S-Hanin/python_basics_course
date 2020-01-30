# -*- coding:utf8 -*-


def closest_to_zero(x):
    return sorted(map(float, x), key=abs)[0]


def user_input():
    return closest_to_zero(input().split())
