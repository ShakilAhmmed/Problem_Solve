# Ask the user to enter the coordinates of a point and find the distance of the point from the origin
# Distance of a point P(x, y) from the origin is given by d(0, P) = sqrt(x2 + y2)
import math

x, y = list(map(int, input().split()))

x_sq = x * x
y_sq = y * y
distance = math.sqrt(x_sq + y_sq)

print(distance)
