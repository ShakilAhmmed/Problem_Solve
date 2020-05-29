# Ask the user to enter two points (x and y coordinates) and find the distance between them.
# Distance between two points P(x1, y1) and Q(x2, y2) is given by: d(P, Q) = p(x2 − x1)2 + (y2 − y1)2 {Distance formula}
import math

x_points1, y_points1 = list(map(int, input().split()))
x_points2, y_points2 = list(map(int, input().split()))

first_form = x_points2 - x_points1
second_form = y_points2 - y_points1
distance = math.sqrt((first_form * first_form) + (second_form * second_form))
print(distance)
