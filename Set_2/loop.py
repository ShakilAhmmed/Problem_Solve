limit = int(input())
for i in range(limit):
    data = input()
    data = list(data)
    sum_data = int(data[0]) + int(data[-1])
    print("Sum =", str(sum_data))
