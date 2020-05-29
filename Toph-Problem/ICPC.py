n = input()
output = {}
for i in n:
	output[int(i)] = n.count(i)
max_value = max(output.values())
max_keys = [k for k, v in output.items() if v == max_value]
print(min(max_keys))