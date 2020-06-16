test_case = int(input())
for i in range(test_case):
	n = int(input())
	numbers = list(map(int, input().split()))
	a = b = 0
	for index, num in enumerate(numbers):
		if index % 2 != num % 2:
			if index % 2 == 0:
				a += 1
			else:
				b += 1
	if a != b:
		print(-1)
	else:
		print(a)

