t = int(input())

for i in range(t):
    n = int(input())
    ans = []
    for j in range(1, n+1):
        if n % j == 0:
            ans.append(str(j))
    print(f"Case {i+1}: "+" ".join(ans))
