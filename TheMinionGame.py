sentence = input()

# consonents
stuart = 0

# vowels
kevin = 0
n = len(sentence)
for i in range(n):
    if sentence[i] in ('A', 'E', 'I', 'O', 'U'):
        kevin += n - i
    else:
        stuart += n - i

if kevin > stuart:
    print('Kevin', kevin)
elif stuart > kevin:
    print('Stuart', stuart)
else:
    print('Draw')
