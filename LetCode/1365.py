numbers = list(map(int, input().split()))
cp = numbers.copy()
cp.sort()
output = []
for i in numbers:
	count = 0
	for j in cp:
		if i > j:
			count += 1
	output.append(count)
print(output)
