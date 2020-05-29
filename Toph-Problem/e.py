t = int(input())
for _ in range(0, t):
    x, y, z = map(int, input().split())
    sum_data = []
    for counter in range(1, z+1):
        if counter == 1:
            sum_data.append(2)
        else:
            mul_data = sum_data[counter-2] * y
            sum_data.append(mul_data)
    print(sum(sum_data))
