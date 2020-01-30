import unittest

import task3_2


class Task32Test(unittest.TestCase):
    def test_should_flatten_iterable(self):
        self.assertListEqual([1, 2, 3], task3_2.flatten([1, [2, [3]]]))

    def test_flatten_returns_none_with_cycled_iterable(self):
        a = [1, 2]
        a.append(a)
        self.assertIsNone(task3_2.flatten(a))

    def test_returns_none_with_cycled_iterable(self):
        a = [1, 2]
        a.append(a)
        self.assertIsNone(task3_2.add_up_and_multiply(a))

    def test_returns_sum_of_positional_args(self):
        a = [1, 2]
        self.assertEqual((3, 2), task3_2.add_up_and_multiply(*a))

    def test_sum_nested_iterables(self):
        a = [1, 2, [2, 3]]
        self.assertEqual((8, 12), task3_2.add_up_and_multiply(a))

    def test_sum_keyword_arguments(self):
        a = {k: v for k, v in zip("abcd", [1, 2, 3, 4])}
        self.assertEqual((10, 24), task3_2.add_up_and_multiply(**a))

    def test_zero_is_skipped(self):
        a = [1, 2, 0]
        self.assertEqual((3, 2), task3_2.add_up_and_multiply(*a))


if __name__ == '__main__':
    unittest.main()
