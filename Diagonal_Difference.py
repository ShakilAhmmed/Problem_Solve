n = int(input())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().rstrip().split())))

first_diagonal = 0
second_diagonal = 0
length = len(matrix[0])
for count in range(length):
    first_diagonal += matrix[count][count]
    second_diagonal += matrix[count][(length-count-1)]
print(abs(first_diagonal-second_diagonal))
