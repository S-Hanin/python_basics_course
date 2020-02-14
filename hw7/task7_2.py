# -*- coding: utf8 -*-

"""
Напишите параметризованный декоратор для классов,
который будет считать и выводить время работы методов класса,
имена которых переданы в параметрах декоратора.
"""
import functools
import logging
import time

logging.basicConfig(level=logging.INFO)


def _measure_time(func):
    @functools.wraps(func)
    def wrap(*m_args, **m_kwargs):
        start = time.time()
        func_result = func(*m_args, **m_kwargs)
        work_time = (time.time() - start) * 1000
        # noinspection Pylint
        logging.info(f"Method `{func.__name__}` has been working: "
                     f"{work_time:.0f} ms")
        return func_result

    return wrap


def time_methods(*args):
    """
    Class decorator. Wraps methods by time measure decorator
    :param args: method names
    """

    def wrap_methods(cls):
        for name in args:
            method = getattr(cls, name)
            if callable(method):
                setattr(cls, name, _measure_time(method))
            else:
                raise TypeError(f"{cls.__name__}.{name} is not callable")
        return cls

    return wrap_methods


@time_methods('foo_test', '__init__', '__new__')
class Baz:
    """
    Class for decorator testing
    """
    a = 1

    def foo_test(self, a_var):
        """
        method for decorator testing
        """
        time.sleep(1)
        print(f"{self.foo_test.__name__}: arg {a_var}")

    def bar_test(self, a_var):
        """
        method for decorator testing
        """
        time.sleep(1)
        print(f"{self.bar_test.__name__}: arg {a_var}")


def main():
    """
    entry point
    """
    baz_test = Baz()
    baz_test.foo_test("hello")
    baz_test.bar_test("world")


if __name__ == '__main__':
    main()
