# -*- coding: utf8 -*-

"""
Напишите параметризованный декоратор, который считает и выводит
при каждом вызове среднее время работы функции за n последних вызовов.
Время выводить в миллисекундах.
"""
import functools
import logging
import time

logging.basicConfig(level=logging.INFO)


def average_time(n: int):
    """
    Decorator. Measures average call time for n last calls
    """
    if n <= 0:
        raise ValueError("Argument must be int > 0")

    def wrap(func):
        counted = []

        @functools.wraps(func)
        def wwrap(*args, **kwargs):
            nonlocal counted
            start = time.time()
            func_result = func(*args, **kwargs)
            counted.append(time.time() - start)
            counted = counted[-n:]
            average = sum(counted) / len(counted) * 1000
            logging.info(f"Среднее время работы: {average:.0f} мс")
            return func_result

        return wwrap

    return wrap


@average_time(2)
def foo(sleep_time):
    time.sleep(sleep_time)
    return sleep_time


if __name__ == '__main__':
    foo(3)
    foo(7)
    foo(1)
    print(foo.__name__)
