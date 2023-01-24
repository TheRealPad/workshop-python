import unittest
from exercice02 import calculate

class TestStringMethods(unittest.TestCase):

    def test_exercice02(self):
        self.assertEqual('foo'.upper(), 'FOO')
        self.assertEqual(calculate(['4', '3', '-2']), 5)
        self.assertEqual(calculate(453), False)
        self.assertEqual(calculate(['nothing', 3, '8', 2, '1']), 9)
        self.assertEqual(calculate('54'), False)

if __name__ == '__main__':
    unittest.main()