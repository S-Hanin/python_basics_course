import unittest
from hw2 import task2


class Task2Test(unittest.TestCase):
    def test_get_odd_number_squares(self):
        self.assertEqual([1, 9, 25], task2.get_odd_number_squares(0, 5))
        self.assertEqual([25, 9, 1, 1, 9, 25], task2.get_odd_number_squares(-5, 5))

    def test_numbers_in_range_divisible_by(self):
        self.assertEqual(3, task2.count_numbers_divisible_by(3, 9, 3))

    def test_factorial_valid_argument(self):
        self.assertEqual(1, task2.factorial(0))
        self.assertEqual(24, task2.factorial(4))

    def test_factorial_invalid_argument(self):
        self.assertRaises(ValueError, task2.factorial, -1)
        self.assertRaises(ValueError, task2.factorial, 3.14)

    def test_range_with_positive_step(self):
        self.assertEqual(list(range(3)), task2.get_range(3))
        self.assertEqual(list(range(3)), task2.get_range(0, 3))
        self.assertEqual(list(range(0, 5, 2)), task2.get_range(0, 5, 2))

    def test_range_with_negative_step(self):
        self.assertEqual(list(range(-3)), task2.get_range(-3))
        self.assertEqual(list(range(5, 0, -2)), task2.get_range(5, 0, -2))
        self.assertEqual(list(range(0, 5, -2)), task2.get_range(0, 5, -2))


if __name__ == '__main__':
    unittest.main()
