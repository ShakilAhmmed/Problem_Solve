numbers = list(map(int, input().split()))
n, m, a = numbers[0], numbers[1], numbers[2]
p = n // a if n % a == 0 else n // a + 1
q = m // a if m % a == 0 else m // a + 1
print(p * q)
