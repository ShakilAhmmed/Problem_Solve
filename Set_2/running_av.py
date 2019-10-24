# limit = int(input())
# sum_data = 0
# val = 0
# for i in range(1, limit + 1):
#     data = float(input())
#     sum_data = sum_data + data
#     val = sum_data / i
#     print(val)
limit = int(input())
li = list(map(int, input().split()))
for i in range(limit):
    # print(li[:i+1])
    print(sum(li[:i+1])/(i+1))
