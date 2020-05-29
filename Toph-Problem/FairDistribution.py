numbers = list(map(int, input().split()))
output = numbers[1]
while int(output) % int(numbers[0]) != 0:
	output += 1
print(abs(numbers[1] - output))
