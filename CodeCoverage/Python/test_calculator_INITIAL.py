
import unittest
from calculator import Calculator

class TestCalculator (unittest.TestCase):
	def setUp(self):
		self.calc = Calculator()

	def test_add(self):
		self.assertEqual(self.calc.add(2,3), 5)

	def test_subtract(self):
		self.assertEqual(self.calc.subtract(10,5), 5)

	def test_divide(self):
		self.assertEqual(self.calc.divide(10,2), 5)
# end-class

if __name__ == "__main__":
	unittest.main()

# Name                         Stmts   Miss  Cover   Missing
# ----------------------------------------------------------
# calculator.py                   25     13    48%   4-10, 20, 24, 28-30, 33
# test_calculator_INITIAL.py      13      0   100%
# ----------------------------------------------------------
# TOTAL                           38     13    66%
