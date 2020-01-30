import unittest

import pprint
import task3_4


class Task34Test(unittest.TestCase):
    def setUp(self) -> None:
        self.xml_string = '<root><element1 /><element2 /><element3><element4 /></element3></root>'
        self.xml_string2 = '<root><element1 /><element2 /><element3><element4><element5 /> </element4></element3></root>'

    def test_xml_to_dict_returns_elements_dict(self):
        expected_tree = {
            'name': 'root',
            'children': [
                {'name': 'element1', 'children': []},
                {'name': 'element2', 'children': []},
                {
                    'name': 'element3',
                    'children': [
                        {'name': 'element4', 'children': []}
                    ]
                }
            ]
        }
        expected_levels = 2
        tree, levels = task3_4.xm_to_dict(self.xml_string)
        self.assertDictEqual(expected_tree, tree)
        self.assertEqual(expected_levels, levels)


if __name__ == '__main__':
    unittest.main()
