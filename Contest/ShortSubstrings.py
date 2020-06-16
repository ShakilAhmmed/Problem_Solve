test_case = int(input())
for i in range(test_case):
	sub_string_b = input()
	output = " "
	first, last = sub_string_b[0], sub_string_b[-1]
	lenght_str = len(sub_string_b) - 2
	output = first
	if lenght_str == 0 or lenght_str < 0:
		output += last
	else:
		j = 1
		while j <= lenght_str:
			output += list(set(sub_string_b[j:j + 2]))[0]
			j = j + 2
		output += last
	print(output)
