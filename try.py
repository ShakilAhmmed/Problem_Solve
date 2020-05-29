t = int(input())

for _ in range(t):
	numbers = list(map(int, input().split()))
	first_negative = numbers[1] - numbers[2]  # a-b
	second_negative = numbers[3] - numbers[4]  # c- d
	first_positive = numbers[1] + numbers[2]  # a+b
	second_positive = numbers[3] + numbers[4]  # c+d
	if ((numbers[0] * first_negative) > second_positive) or ((numbers[0] * first_positive) < second_negative):
		print("No")
	else:
		print("Yes")
