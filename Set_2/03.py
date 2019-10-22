take_input = [x for x in input().split()]
count = 0
for value in take_input:
    if len(value) >= 2 and value[0] == value[-1]:
        count += 1

print(count)
