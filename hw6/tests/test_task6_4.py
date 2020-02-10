import unittest

from task6_4 import cycle


def limit_cycle(collection, limit):
    result = []
    g = cycle(collection)
    for item in range(len(collection) * limit):
        result.append(next(g))
    return result


class Task64Test(unittest.TestCase):
    def test_returns_elements_n_times(self):
        expected = [1, 2, 1, 2]
        actual = list(limit_cycle([1, 2], 2))
        self.assertListEqual(expected, actual)

    def test_correct_work_with_empty_collections(self):
        expected = []
        actual = list(limit_cycle([], 2))
        self.assertListEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
