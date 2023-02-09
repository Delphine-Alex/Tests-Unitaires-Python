import unittest

if __name__ == '__main__':
    unittest.main()

from app.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(6, 2), 8)
        self.assertEqual(Calculator.add(0, 0), 0)
        self.assertEqual(Calculator.add(-6, 2), -4)
        self.assertEqual(Calculator.add(-6, -2), -8)
        
    def test_subtract(self):
        self.assertEqual(Calculator.subtract(6, 2), 4)
        self.assertEqual(Calculator.subtract(0, 0), 0)
        self.assertEqual(Calculator.subtract(-6, 2), -8)
        self.assertEqual(Calculator.subtract(-6, -2), -4)
        
    def test_multiply(self):
        self.assertEqual(Calculator.multiply(0, 0), 0)
        self.assertEqual(Calculator.multiply(0, 2), 0)
        self.assertEqual(Calculator.multiply(6, 0), 0)
        self.assertEqual(Calculator.multiply(6, 2), 12)
        self.assertEqual(Calculator.multiply(-6, -2), 12)
        self.assertEqual(Calculator.multiply(-6, 2), -12)
        
    def test_divide(self):
        self.assertEqual(Calculator.divide(6, 2), 3)
        self.assertEqual(Calculator.divide(-6, -2), 3)
        self.assertEqual(Calculator.divide(6, -2), -3)
        with self.assertRaises(ZeroDivisionError):
            Calculator.divide(6, 0)
        with self.assertRaises(ZeroDivisionError):
            Calculator.divide(0, 0)
        
    def test_power(self):
        self.assertEqual(Calculator.power(2, 6), 64)
        self.assertEqual(Calculator.power(-2, 6), -64)
        self.assertEqual(Calculator.power(0, 0), 1)
        self.assertEqual(Calculator.power(6, 0), 1)
        self.assertEqual(Calculator.power(0, 2), 0)
        
    def test_square_root(self):
        self.assertEqual(Calculator.square_root(4), 2)
        self.assertEqual(Calculator.square_root(16), 4)
