number, times = list(map(int, input().split()))
_tnumber = number
for i in range(times):
	last_digit = _tnumber % 10
	if last_digit != 0:
		_tnumber -= 1
	else:
		_tnumber = _tnumber // 10
print(_tnumber)