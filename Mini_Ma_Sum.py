
numbers = list(map(int, input().split()))
sum_data = 0

for x in range(len(numbers)):
    sum_data += numbers[x]
print(sum_data-max(numbers), sum_data - min(numbers))
