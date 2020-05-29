n = int(input())
first_number = 1
second_number = 1
fib = [first_number, second_number]
for i in range(n):
	temp = first_number + second_number
	first_number = second_number
	second_number = temp
	fib.append(temp)
print(fib[n - 1])
