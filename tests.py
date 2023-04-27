#!/usr/bin/env python
import unittest

class Testing(unittest.TestCase):
    def test_string(self):
        a = 'some'
        b = 'some'
        self.assertEqual(a, b)

    def test_boolean(self):
        a = True
        b = True
        self.assertEqual(a, b)

    def test_new_string(self):
        a = 'Chuck'
        b = 'Charles'
        self.assertNotEqual(a, b)

    def nums_is_nums(self):
        a = 97
        b = 55
        self.assertGreater(a, b)

if __name__ == '__main__':
    unittest.main()
