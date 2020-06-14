n = input()
output = ''
for i, value in enumerate(n):
	if i == 0:
		output += value.upper()
	else:
		output += value
print(output)