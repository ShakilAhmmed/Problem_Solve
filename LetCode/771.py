def numJewelsInStones(J: str, S: str) -> int:
	count = 0
	for i in S:
		if i in J:
			count += 1
	return count


j = input()
s = input()
print(numJewelsInStones(j, s))
