t = int(input())
for i in range(t):
    data = map(int, input().split())
    print(f"Case {i+1}: {sorted(data, reverse=True)[1]}")
