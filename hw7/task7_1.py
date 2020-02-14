# -*- coding: utf8 -*-

"""
Напишите параметризованный декоратор, который считает и выводит
при каждом вызове среднее время работы функции за n последних вызовов.
Время выводить в миллисекундах.
"""
import functools
import logging
import time
from collections import deque

logging.basicConfig(level=logging.INFO)


def average_time(calls_count: int):
    """
    Decorator. Measures average call time for n last calls
    """
    if calls_count <= 0:
        raise ValueError("Argument must be int > 0")

    def wrap(func):
        counted = deque(maxlen=calls_count)

        @functools.wraps(func)
        def wwrap(*args, **kwargs):
            nonlocal counted
            start = time.time()
            func_result = func(*args, **kwargs)
            counted.append(time.time() - start)
            average = sum(counted) / len(counted) * 1000
            # noinspection Pylint
            logging.info(f"Среднее время работы {func}: {average:.0f} мс")
            return func_result

        return wwrap

    return wrap


@average_time(2)
def foo_test(sleep_time):
    """
    Decorator work test
    """

    time.sleep(sleep_time)
    return sleep_time


if __name__ == '__main__':
    foo_test(3)
    foo_test(7)
    foo_test(1)
