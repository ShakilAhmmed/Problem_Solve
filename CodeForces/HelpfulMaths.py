s = input()
output = []
for i in s:
	if i != "+":
		output.append(int(i))
output = sorted(output)
print("+".join(map(str, output)))
