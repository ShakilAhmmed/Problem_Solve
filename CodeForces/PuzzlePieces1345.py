t = int(input())
for _ in range(t):
	n, m = input().split()
	if int(n) == 1 or int(m) == 1:
		print("YES")
	elif int(n) == 2 and int(m) == 2:
		print("YES")
	else:
		print("NO")
