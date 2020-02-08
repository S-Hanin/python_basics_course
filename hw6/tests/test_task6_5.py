import unittest

from task6_5 import chain


class Task65Test(unittest.TestCase):
    def test_accept_variable_amount_of_collections(self):
        self.assertListEqual([1, 2], list(chain([1], [2])))
        self.assertListEqual([1, 2, 3], list(chain([1], [2], [3])))

    def test_works_correct_with_empty_collections(self):
        self.assertListEqual([], list(chain([], [])))
        self.assertListEqual([1], list(chain([], [1])))


if __name__ == '__main__':
    unittest.main()
