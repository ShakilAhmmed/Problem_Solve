l, b = list(map(int, input().split()))
l_weight = l
b_weight = b
year = 0
while l_weight <= b_weight:
	year += 1
	l_weight *= 3
	b_weight *= 2
print(year)