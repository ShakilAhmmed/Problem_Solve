number = input().split()
science_check = float(number[0]) >= 4.00 and number[1] == "science"
commerce_check = float(number[0]) >= 3.00 and number[1] == "commerce"
humanities_check = float(number[0]) >= 2.50 and number[1] == "humanities"
if science_check or commerce_check or humanities_check:
	print("Welcome to RCCIPSC family.")
else:
	if float(number[0]) >= 3.00:
		print("Your GPA is low. You can study in commerce department.")
	elif float(number[0]) >= 2.50:
		print("Your GPA is low. You can study in humanities department.")
	else:
		print("Try out another college.")
