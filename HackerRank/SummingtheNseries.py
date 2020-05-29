def summingSeries(n):
	return (n * n) % 1000000007


t = int(input())
for _ in range(t):
	number = int(input())
	print(summingSeries(number))
