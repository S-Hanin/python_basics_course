import unittest

from task6_2 import get_public_attributes


class Task62Test(unittest.TestCase):
    def setUp(self) -> None:
        cls = type("ClassForTest", (), {})
        self.obj = object.__new__(cls)
        self.obj.__dict__.update({'a': 1, 'b': "hello"})

    def test_returns_public_attributes(self):
        self.assertListEqual(['a', 'b'], get_public_attributes(self.obj))


if __name__ == '__main__':
    unittest.main()
