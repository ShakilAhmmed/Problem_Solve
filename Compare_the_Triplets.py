a = list(map(int, input().split()))
b = list(map(int, input().split()))
alice_point = 0
bob_point = 0

for counter in range(3):
    if a[counter] > b[counter]:
        alice_point += 1
    elif a[counter] < b[counter]:
        bob_point += 1
print(alice_point, bob_point)
