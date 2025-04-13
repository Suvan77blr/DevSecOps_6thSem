
import unittest
from calculator import Calculator

class TestCalculator (unittest.TestCase):
	def setUp(self):
		self.calc = Calculator()

	def test_add(self):
		# self.assertEqual(self.calc.add(2,3), 5)
		self.assertEqual(self.calc.operate(2, 3,'+'), 5)

	def test_subtract(self):
		# self.assertEqual(self.calc.subtract(10,5), 5)
		self.assertEqual(self.calc.operate(10,5,'-'), 5)

	def test_multiply(self):
		# self.assertEqual(self.calc.multiply(4,3), 12)
		self.assertEqual(self.calc.operate(4,3,'*'), 12)

	def test_divide(self):
		# self.assertEqual(self.calc.divide(10,2), 5)
		self.assertEqual(self.calc.operate(10,2,'/'), 5)

	def test_divide_by_zero(self):
		with self.assertRaises(ValueError):
			# self.calc.divide(7, 0)
			self.calc.operate(7, 0,'/')
	
	def test_modulus(self):
		# self.assertEqual(self.calc.modulus(21, 4), 1)
		self.assertEqual(self.calc.operate(21, 4, '%'), 1)

	def test_modulus_by_zero(self):
		with self.assertRaises(ValueError):
			# self.calc.modulus(10, 0)
			self.calc.operate(10, 0, '%')

	def test_power(self):
		# self.assertEqual(self.calc.power(2, 10), 1024)
		self.assertEqual(self.calc.operate(2, 10, '^'), 1024)
# end-class


if __name__ == "__main__":
	unittest.main()

# Name                       Stmts   Miss  Cover   Missing
# --------------------------------------------------------
# calculator.py                 25      7    72%   4-10
# test_calculator_FINAL.py      25      0   100%
# --------------------------------------------------------
# TOTAL                         50      7    86%
