limit = int(input())
result = []
for i in range(1, limit + 1):
    data = input()
    if data.lower() == data[::-1].lower():
        result.append("Yes")
    else:
        result.append("No")
print('\n'.join(result))
