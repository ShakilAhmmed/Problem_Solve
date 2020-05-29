n, m = map(int, input().split())
string_one = '.|.'
string_two = "WELCOME"

for i in range(n // 2):
	print((string_one * ((i * 2) + 1)).center(m, '-'))
print(string_two.center(m, '-'))
for i in range(n // 2-1, -1, -1):
	print((string_one * ((i * 2) + 1)).center(m, '-'))
