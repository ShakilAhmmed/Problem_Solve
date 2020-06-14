k, n, w = input().split()
total_amount = 0
for i in range(1, int(w) + 1):
	total_amount += (int(k) * i)
ans = max(total_amount - int(n), 0)
print(ans)
