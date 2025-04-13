# Src Code.
class Calculator:
	def operate(self, a, b, op):
		if(op == '+'): 		return self.add(a, b)
		elif(op == '-'):    return self.subtract(a, b)
		elif(op == '*'):	return self.multiply(a, b)
		elif(op == '/'):    return self.divide(a, b)
		elif(op == '%'):	return self.modulus(a, b)
		elif(op == '^'):	return self.power(a, b)
		else: return "Invalid Operation!"
	#end-function.

	def add(self, a, b):
		return a + b	

	def subtract(self, a, b):
		return a - b	

	def multiply(self, a, b):
		return a * b	

	def divide(self, a, b):
		if (b == 0):
			raise ValueError("Zero division error!")
		return (a / b)

	def modulus(self, a, b):		
		if (b == 0):
			raise ValueError("Zero division error!")
		return (a % b)
	
	def power(self, a, b):
		return a ** b	
#end-class

# Name                      Stmts   Miss  Cover   Missing
# -------------------------------------------------------
# calculator.py                25      1    96%   10
# test_calculator_FULL.py      25      0   100%
# -------------------------------------------------------
# TOTAL                        50      1    98%
