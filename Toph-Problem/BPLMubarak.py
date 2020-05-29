t = int(input())
for _ in range(t):
	balls_input = input()
	total_balls = 0
	for ball in balls_input:
		if ball != "N" and ball != "W" and ball != "D":
			total_balls += 1
	over = total_balls // 6
	balls = total_balls % 6
	if balls == 0 and over != 0:
		if over > 1:
			output = "OVERS"
		else:
			output = "OVER"
		print("{} {}".format(over, output))
	elif over == 0 and balls != 0:
		if balls > 1:
			output = "BALLS"
		else:
			output = "BALL"
		print("{} {}".format(balls, output))
	else:
		if over > 1:
			over_output = "OVERS"
		else:
			over_output = "OVER"
		if balls > 1:
			ball_output = "BALLS"
		else:
			ball_output = "BALL"
		print("{} {} {} {}".format(over, over_output, balls, ball_output))
