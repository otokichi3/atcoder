import unittest
from a0 import binsearch

class A0Test(unittest.TestCase):
    def test_returns_int(self):
        a = [1, 2, 3, 5, 6, 11, 13]
        k = 3
        res = binsearch(a, k)
        self.assertTrue(isinstance(res, int))

    def test_returns_index(self):
        a = [1, 2, 3, 5, 6, 11, 13]
        k = 3
        res = binsearch(a, k)
        self.assertEqual(res, 2)

if __name__ == "__main__":
    unittest.main()