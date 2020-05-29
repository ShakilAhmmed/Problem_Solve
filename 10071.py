while True:
	try:
		v, t = map(int, input().split())
	except EOFError:
		break
		
	print(2 * v * t)