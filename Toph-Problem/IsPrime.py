n = int(input())
ans = True
if n == 1:
	ans = False
else:
	for i in range(2, n):
		if n > 1 and n % i == 0:
			ans = False
			break
		else:
			ans = True
print("Yes" if ans else "No")
