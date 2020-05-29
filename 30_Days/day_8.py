t = int(input())

phone_book = {}
for i in range(t):
    data = input().split()
    phone_book[data[0]] = data[1]
while True:
    try:
        n = input()
        data = phone_book.get(n, None)
        if data is not None:
            print(f"{n}={data}")
        else:
            print("Not found")
    except EOFError:
        break
