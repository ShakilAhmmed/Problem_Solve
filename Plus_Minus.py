n = int(input())
arr = list(map(int, input().rstrip().split()))
count_positive, count_negative,  count_zero = 0, 0, 0
for x in arr:
    if x > 0:
        count_positive += 1
    elif x < 0:
        count_negative += 1
    elif x == 0:
        count_zero += 1
print(count_positive/len(arr))
print(count_negative/len(arr))
print(count_zero/len(arr))
