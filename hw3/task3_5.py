# -*- coding:utf8 -*-


def closest_to_zero(X):
    return sorted(map(float, X), key=abs)[0]


def user_input():
    return closest_to_zero(input().split())
