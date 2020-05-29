from typing import List


def findThePoint(px: int, py: int, qx: int, qy: int) -> List:
	rx = 2 * qx - px
	ry = 2 * qy - py
	return [rx, ry]


t = int(input())
for _ in range(t):
	px, py, qx, qy = map(int, input().split())
	result = findThePoint(px, py, qx, qy)
	print(f"{result[0]} {result[1]}")
