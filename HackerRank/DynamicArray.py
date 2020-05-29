n, q = list(map(int, input().split()))
seqList = []
for i in range(n):
	seqList.append([])
lastAnswer = 0
for j in range(q):
	numbers = list(map(int, input().split()))
	x, y = numbers[1], numbers[2]
	if numbers[0] == 1:
		index = (x ^ lastAnswer) % n
		seqList[index].append(y)
	else:
		index = (x ^ lastAnswer) % n
		size = y % len(seqList[index])
		lastAnswer = seqList[index][size]
		print(lastAnswer)
