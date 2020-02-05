import unittest

from task5_3 import Observable


class Task53Test(unittest.TestCase):
    def setUp(self) -> None:
        cls = type("A", (Observable,), {})
        self.obj = cls(a=1, b=[1, 2], c="hello")

    def test_str_representation(self):
        self.assertEqual("A(a=1, b=[1, 2], c='hello')", str(self.obj))


if __name__ == '__main__':
    unittest.main()
