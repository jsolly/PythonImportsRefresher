import unittest
from Package1 import module1
class TestStringMethods(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(module1.multiply(10,10), 100)