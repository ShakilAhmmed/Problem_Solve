limit = int(input())
for i in range(limit):
    numbers = list(map(int, input().split()))
    avg = int(sum(numbers[1:]) / numbers[0])
    greater_len = len(list(filter(lambda x: x > avg, numbers)))
    result = float((100 * greater_len) / numbers[0])
    print("{0:.3f}%".format(result))
