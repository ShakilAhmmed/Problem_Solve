n = int(input())


def fact(n):
	if n == 0:
		return 1
	else:
		return n * fact(n - 1)


output = str(fact(n))
print(output[-4:])
