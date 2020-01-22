# -*-coding: utf8-*-

import unittest
import hw1.service as service


class Task1Test(unittest.TestCase):

    def test_task1_first_letter_is_uppercase(self):
        self.assertEqual("Alison Heck", service.capitalize("alison heck"))

    def test_task2_character_frequency(self):
        should_be = {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
        self.assertEqual(should_be, service.count_frequency("google.com"))

    def test_task3_cut_middle_of_string(self):
        self.assertEqual("w3ce", service.cut_middle_chars("w3resource"))
        self.assertEqual("w3w3", service.cut_middle_chars("w3"))
        self.assertEqual("", service.cut_middle_chars(" w"))

    def test_task4_count_strings_where_first_and_last_letters_are_equal(self):
        self.assertEqual(2, service.count_words(['abc', 'xyz', 'aba', '1221']))
        self.assertEqual(0, service.count_words(['abc', 'xyz']))

    def test_task5_is_subset(self):
        self.assertTrue(service.is_subset({1, 2}, {2, 3}, {2}))
        self.assertFalse(service.is_subset({1, 2}, {3, 4}, {5}))

    def test_task6_generate_dict(self):
        should_be = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
        self.assertEqual(should_be, service.generate_squares(5))

    def test_task7_merge_dicts(self):
        should_be = {"a": 1, "b": 2}
        self.assertEqual(should_be, service.merge_dicts({"a": 1}, {"b": 2}))

    def test_task8_find_highest_three_values_in_dict(self):
        should_be = [9, 16, 25]
        test_data = service.generate_squares(5)
        self.assertEqual(should_be, service.get_highest_three_values(test_data))
        self.assertRaises(AssertionError,
                          service.get_highest_three_values,
                          service.generate_squares(2))
        with self.assertRaises(AssertionError):
            service.get_highest_three_values(service.generate_squares(2))

    def test_task9_remove_duplicates_from_list(self):
        self.assertEqual([1, 2, 3], service.remove_duplicates([1, 1, 2, 2, 3]))

    def test_task10_get_difference(self):
        self.assertEqual([4, 4, 3], service.get_difference([1, 2, 4, 4], [1, 2, 3]))
