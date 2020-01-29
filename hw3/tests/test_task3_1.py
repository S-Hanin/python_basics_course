import unittest

from hw3 import task3_1


class Task3_1_Test(unittest.TestCase):
    def test_get_squares(self):
        self.assertListEqual([0, 1, 4, 9], task3_1.get_squares(list(range(4))))

    def test_get_even_elements(self):
        self.assertListEqual([-2, 0, 2, 4], task3_1.get_even_positioned_elements(list(range(-2, 6))))

    def test_get_cubes_of_evens(self):
        self.assertListEqual([8], task3_1.get_cubes_of_evens([0, 2, 3]))
        self.assertListEqual([0], task3_1.get_cubes_of_evens([2, 0, 3]))


if __name__ == '__main__':
    unittest.main()
