n = int(input())
count = 0
for _ in range(n):
	number = list(map(int, input().split()))
	one_count = number.count(1)
	zero_count = number.count(0)
	if one_count > zero_count:
		count += 1
print(count)
