n, d = list(map(int, input().split()))
numbers = list(map(int, input().split()))
for i in range(d):
	_temp = numbers[0]
	numbers.remove(_temp)
	numbers.append(str(_temp))
print(" ".join(map(str, numbers)))
