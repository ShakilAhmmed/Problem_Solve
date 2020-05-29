while True:
	Number = int(input())
	if Number == 0:
		break
	else:
		count = 0
		for i in range(2, Number + 1):
			if Number % i == 0:
				isprime = 1
				for j in range(2, (i // 2 + 1)):
					if i % j == 0:
						isprime = 0
						break

				if isprime == 1:
					count += 1
		print(f"{Number} : {count}")
