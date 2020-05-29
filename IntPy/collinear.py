# Ask the user to enter three points and find whether they are collinear
# Formula : x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
x1, x2, x3, y1, y2, y3 = list(map(int, input().split()))
formula = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
is_col = "Yes" if formula == 0 else "No"
print(is_col)
