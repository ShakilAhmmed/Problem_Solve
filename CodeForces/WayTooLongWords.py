t = int(input())
for _ in range(t):
	lines = input()
	if len(lines) <= 10:
		print(lines)
	else:
		count = 0
		for line in lines[1:len(lines) - 1]:
			count += 1
		print(f"{lines[0]}{count}{lines[len(lines) - 1]}")
