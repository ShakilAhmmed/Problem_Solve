name = input()
non_duplicates = []
for i in name:
	if i not in non_duplicates:
		non_duplicates.append(i)
count = len(non_duplicates)
if count % 2 != 0:
	print("IGNORE HIM!")
else:
	print("CHAT WITH HER!")

