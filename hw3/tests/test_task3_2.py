import unittest

from hw3 import task3_2


class Task32Test(unittest.TestCase):
    def test_should_flatten_iterable(self):
        self.assertListEqual([1, 2, 3], task3_2.flatten([1, [2, [3]]]))

    def test_first_level_cycled_iterable(self):
        a = [1, 2]
        a.append(a)
        self.assertTrue(task3_2.is_cycled_iterable(a))

    def test_second_level_cycled_iterable(self):
        a = [1, 2]
        b = [3, 4]
        a.append(b)
        b.append(a)
        self.assertTrue(task3_2.is_cycled_iterable(a))

    def test_returns_none_with_cycled_iterable(self):
        a = [1, 2]
        a.append(a)
        self.assertIsNone(task3_2.add_up_and_multiply(a))

    def test_returns_sum_and_product_of_positional_args(self):
        a = [1, 2]
        self.assertEqual((3, 2), task3_2.add_up_and_multiply(*a))

    def test_returns_sum_and_product_of_nested_iterables(self):
        a = [1, 2, [2, 3]]
        self.assertEqual((8, 12), task3_2.add_up_and_multiply(a))

    def test_returns_sum_and_product_of_keyword_arguments(self):
        a = dict(zip("abcd", [1, 2, 3, 4]))
        self.assertEqual((10, 24), task3_2.add_up_and_multiply(**a))

    def test_zero_is_skipped(self):
        a = [1, 2, 0]
        self.assertEqual((3, 2), task3_2.add_up_and_multiply(*a))


if __name__ == '__main__':
    unittest.main()
