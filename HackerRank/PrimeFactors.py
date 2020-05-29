primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
t = int(input())
for _ in range(t):
	number = int(input())
	product = 1
	ans = 0
	for i in range(15):
		product = product * primes[i]
		if product <= number:
			ans += 1

	print(ans)
