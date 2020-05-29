matrix = []
for _ in range(5):
	numbers = list(map(int, input().split()))
	matrix.append(numbers)

for index, data in enumerate(matrix):
	for in_index, value in enumerate(data):
		if value == 1:
			output = abs(2 - index) + abs(in_index - 2)
			print(output)
