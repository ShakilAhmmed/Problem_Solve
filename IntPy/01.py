x, y = list(map(int, input().split()))
# Say x=20 y=30
# x = x + y  # Now x = 20 + 30 = 50
# y = x - y  # Now y = 50 - 30 = 20
# x = x - y  # Now x = 50 - 20 = 30 So x is 30 y is 20
# print(f"X = {x} and Y = {y}")

# Another Way
x, y = y, x
print(f"X = {x} and Y = {y}")
