import math


def findHeight(b: int, a: int) -> int:
	return math.ceil((2 * a) / b)


numbers = list(map(int, input().split()))
print(findHeight(numbers[0], numbers[1]))
