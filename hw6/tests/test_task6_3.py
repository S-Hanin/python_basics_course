import unittest

from task6_3 import associate


class Task63Test(unittest.TestCase):
    def test_correct_with_equal_size_lists(self):
        expected = {'a': 1}
        actual = associate(['a'], [1])
        self.assertDictEqual(expected, actual)

    def test_value_is_none_if_key_exists_but_value_is_absent(self):
        expected = {'a': None}
        actual = associate(['a'], [])
        self.assertDictEqual(expected, actual)

    def test_values_dropped_if_key_is_absent(self):
        expected = {'a': 1}
        actual = associate(['a'], [1, 2])
        self.assertDictEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
