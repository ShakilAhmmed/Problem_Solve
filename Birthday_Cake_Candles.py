n = int(input())

candles = list(map(int, input().split()))

max_digit = max(candles)

count_digit = candles.count(max_digit)

print(count_digit)
