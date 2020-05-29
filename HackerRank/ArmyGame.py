def gameWithCells(n, m):
	n += 1 if n % 2 else 0
	m += 1 if m % 2 else 0
	return (n * m) // 4


numbers = list(map(int, input().split()))
print(gameWithCells(numbers[0], numbers[1]))
