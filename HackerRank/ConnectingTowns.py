def connectingTowns(n, routes):
	path = 1
	for i in routes:
		path = (path * i) % 1234567
	return path


t = int(input())
for _ in range(t):
	towns = int(input())
	routes = list(map(int, input().split()))
	print(connectingTowns(towns, routes))
