limit = int(input())
for i in range(limit):
    data = input()
    count = 0
    for x in data:
        if x.lower() in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    print("Number of vowels = {0}".format(count))
