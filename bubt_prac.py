
while True:
    try:
        d, m = map(int, input().split())
        if d == 7 and m == 1:
            print("Happy Birthday To Shipu.")
        elif d == 29 and m == 4:
            print("Happy Birthday To Dipu Sir.")
        elif d == 30 and m == 5:
            print("Happy Birthday To Fahad vai.")
        elif d == 21 and m == 6:
            print("Happy Birthday To Sufian.")
        elif d == 11 and m == 12:
            print("Happy Birthday To Alim.")
        else:
            print("This is an ordinary day.")
    except EOFError:
        break
