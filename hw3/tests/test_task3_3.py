import unittest

from hw3 import task3_3


class Task3_3_Test(unittest.TestCase):
    def test_average(self):
        self.assertEqual((1.0, 1), task3_3.average(1, 1, 1, 1))

    def test_returns_max_number_between_calls(self):
        self.assertEqual((1.0, 1), task3_3.average(1, 1, 1, 1))
        self.assertEqual((4.0, 13), task3_3.average(1, 1, 1, 13))
        self.assertEqual((2.0, 13), task3_3.average(1, 1, 1, 5))


if __name__ == '__main__':
    unittest.main()
