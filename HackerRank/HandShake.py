def handShake(n: int) -> int:
	return ((n - 1) * n) // 2


t = int(input())
for _ in range(t):
	n = int(input())
	print(handShake(n))

