sentence = "aWESOME is cODING"

data = sentence.split(" ")
data.reverse()
result = []
for value in data:
	output = ""
	for text in value:
		if text.islower():
			output += text.upper()
		else:
			output += text.lower()
	result.append(output)
print(" ".join(result))
