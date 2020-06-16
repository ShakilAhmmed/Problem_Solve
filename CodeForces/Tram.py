stops = int(input())
total_seat = 0
seats_av = []
for i in range(stops):
	exit_seat, arrive_seat = list(map(int, input().split()))
	total_seat += (arrive_seat - exit_seat)
	seats_av.append(total_seat)
print(max(seats_av))
