import unittest
import calc
import math


class TestCalc(unittest.TestCase):

    def test_cosine(self):
        self.assertEqual(calc.cosine(math.pi/2), 0)
        self.assertEqual(calc.cosine(0), 1)
        self.assertEqual(calc.cosine(math.pi/3), 0.5)

    def test_sine(self):
        self.assertEqual(calc.sine(math.pi/2), 1)
        self.assertEqual(calc.sine(0), 0)
        self.assertEqual(calc.sine(math.pi/6), 0.5)

    def test_power(self):
        self.assertEqual(calc.power(2, 3), 8)
        self.assertEqual(calc.power(-4, 2), 16)
        self.assertEqual(calc.power(3, 2), 9)

    def test_logarithm(self):
        self.assertEqual(calc.logarithm(10), 2.3)
        self.assertEqual(calc.logarithm(100), 4.6)
        self.assertEqual(calc.logarithm(1000), 6.9)
        self.assertEqual(calc.logarithm(10000), 9.2)

        with self.assertRaises(ValueError):
            calc.logarithm(-10)


if __name__ == '__main__':
    unittest.main()