import unittest

from task6_1 import EvenIterator


class Task61Test(unittest.TestCase):
    def test_returns_even_positioned_elements(self):
        iterable = list(range(10))
        expected = [x for x in range(10) if x % 2 == 0]
        self.assertListEqual(expected, list(EvenIterator(iterable)))

    def test_raises_stop_iteration_exception(self):
        iterable = [1]
        iterator = EvenIterator(iterable)
        with self.assertRaises(StopIteration):
            next(iterator)
            next(iterator)


if __name__ == '__main__':
    unittest.main()
