# -*-coding: utf8-*-
import argparse
import service


# You are given with 3 sets, find if third set is a subset of the first and the second sets
# Input: `set([1,2]), set([2,4), set([2])`
# Expected result: `True`
# Input: `set([1,2]), set([3,4), set([5])`
# Expected result: `False`


def main():
    a, b, c = {1, 2}, {2, 3}, {2}
    print(f"{c} is subset of {a} {b}: {service.is_subset(a, b, c)}")

    a, b, c = {1, 2}, {3, 4}, {5}
    print(f"{c} is subset of {a} {b}: {service.is_subset(a, b, c)}")


if __name__ == '__main__':
    main()
