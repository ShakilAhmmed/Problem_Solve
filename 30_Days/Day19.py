class AdvancedArithmetic():
	def divisorSum(n):
		raise NotImplementedError


class Calculator(AdvancedArithmetic):
	def divisorSum(self, n):
		x = []
		for i in range(1, n + 1):
			if n % i == 0:
				x.append(i)

		# print("I implemented: AdvancedArithmetic")
		return sum(x)


obj = Calculator()
print(obj.divisorSum(6))
