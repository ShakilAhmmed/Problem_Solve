n = int(input())

arr = list(map(int, input().rstrip().split()))
rev = arr[::-1]
output = [str(i) for i in rev]
print(" ".join(output))
