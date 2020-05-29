
time_input = input()

time_get = time_input.split(":")

if time_get[-2:] == "PM":
    if time_get[0] != "12":
        time_get[0] = str(int(time_get[0])+12)
    else:
        if time_get[0] == "12":
            time_get[0] = "00"
    ntime = ':'.join(time_get)
    print(str(ntime[:-2]))
