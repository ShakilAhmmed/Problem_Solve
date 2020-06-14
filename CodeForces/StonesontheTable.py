n = int(input())
colors = input()
repeat = 0
for i in range(1, n):
	if colors[i] == colors[i - 1]:
		repeat += 1
print(repeat)
