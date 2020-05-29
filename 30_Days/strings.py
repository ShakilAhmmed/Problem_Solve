test_case = int(input())
for _ in range(test_case):
    data = input()
    even = ''
    odd = ''
    for index, value in enumerate(data):
        if index % 2 == 0:
            even += data[index]
        else:
            odd += data[index]
    print(f"{even} {odd}")
