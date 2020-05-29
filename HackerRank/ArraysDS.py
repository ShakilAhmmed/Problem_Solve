n = int(input())
numbers = list(map(int, input().split()))
numbers.reverse()
print(" ".join(map(str, numbers)))
