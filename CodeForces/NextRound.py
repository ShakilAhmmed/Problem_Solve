n, k = list(map(int, input().split()))
numbers = list(map(int, input().split()))
count = 0
for i in range(len(numbers)):
	if numbers[i] >= numbers[k - 1] and numbers[i] > 0:
		count += 1
print(count)
