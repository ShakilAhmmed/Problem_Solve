t = int(input())
for _ in range(t):
	numbers = list(map(int, input().split()))
	avg = sum(numbers) // len(numbers)
	if avg % 2 == 0:
		print("Sadia will be happy.")
	else:
		print("Oops!")
