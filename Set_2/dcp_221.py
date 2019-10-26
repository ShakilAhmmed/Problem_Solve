limit = int(input())
for i in range(limit):
    data = list(map(int, input().split()))
    max_data = max(data)
    min_data = min(data)
    print("Case {0}: Among {1} numbers {2} is maximum and {3} is minimum".format(i + 1, len(data), max_data, min_data))
