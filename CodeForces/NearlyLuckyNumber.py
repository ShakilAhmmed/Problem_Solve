n = int(input())
flag = 0
for i in str(n):
	i = int(i)
	if i == 4 or i == 7:
		flag += 1
if flag == 4 or flag == 7:
	print("YES")
else:
	print("NO")
