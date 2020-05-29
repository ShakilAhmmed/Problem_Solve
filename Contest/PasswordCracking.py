import random
import string


def randomString(stringLength = 8):
	letters = string.ascii_uppercase
	return ''.join(random.choice(letters) for i in range(stringLength))


for i in range(1, 27):
	print(randomString())
	t = input()
	if t == "ACCESS GRANTED.":
		break
