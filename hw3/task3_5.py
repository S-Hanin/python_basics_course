# -*- coding:utf8 -*-


def closest_to_zero(X):
    return min({abs(float(x)): x for x in X})


def user_input():
    return closest_to_zero(input().split())
