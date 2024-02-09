#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer_base(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_max_integer_nombres_negatifs(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_max_integer_nombres_mixtes(self):
        self.assertEqual(max_integer([-1, 2, -3, 4, -5]), 4)

    def test_max_integer_liste_vide(self):
        self.assertIsNone(max_integer([]))

    def test_max_integer_element_unique(self):
        self.assertEqual(max_integer([42]), 42)

    def test_max_integer_valeurs_dupliquées(self):
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_max_integer_nombres_flottants(self):
        self.assertEqual(max_integer([1.5, 2.8, 0.7]), 2.8)

    def test_max_integer_chaines(self):
        self.assertEqual(max_integer(["pomme", "banane", "orange"]), "orange")

    def test_max_integer_types_mixtes(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, "trois", 4, 5])

if __name__ == '__main__':
    unittest.main()
