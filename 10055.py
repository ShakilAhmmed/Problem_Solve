while True:
    try:
        x,y = map(int,input().split())
    except EOFError:
        break
    print(abs(x-y))