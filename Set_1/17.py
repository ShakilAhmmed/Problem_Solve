first_number, second_number = input().split()
if int(first_number) == 11:
    first_number = 1
if int(second_number) == 11:
    second_number = 1
do_sum = int(first_number) + int(second_number)
if do_sum > 21:
    print("Greater Than 21")
elif do_sum == 21:
    print("Equal To 21")
