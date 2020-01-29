import unittest

from hw3 import task3_5


class Task3_5_Test(unittest.TestCase):
    def test_closest_to_zero(self):
        self.assertEqual(0, task3_5.closest_to_zero([-1, 0, 0.5, 1, 3]))
        self.assertEqual(-1.0, task3_5.closest_to_zero([-1, 1, 3]))
        self.assertEqual(0.5, task3_5.closest_to_zero([0.5, 0.50000000000000000000001]))


if __name__ == '__main__':
    unittest.main()
