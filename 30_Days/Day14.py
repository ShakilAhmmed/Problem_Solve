class Difference:
	def __init__(self, a):
		self.__elements = a
		self.maximumDifference = 0

	def computeDifference(self):
		self.__elements.sort()
		self.maximumDifference = abs(self.__elements[0] - self.__elements[len(self.__elements) - 1])


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
