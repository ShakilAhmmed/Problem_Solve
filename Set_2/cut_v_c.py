# limit = int(input())
# for i in range(limit):
#     data = input()
#     data = list(data)
#     vowel = [x for x in data if x.lower() in ['a', 'e', 'i', 'o', 'u'] if x != ' ']
#     constant = [x for x in data if x.lower() not in ['a', 'e', 'i', 'o', 'u'] if x != ' ']
#     print(''.join(vowel))
#     print(''.join(constant))

T = int(input())
for i in range(1, T + 1):
    string = input()
    vowels = "AEIOUaeiou"
    consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    s_vowel = ''
    s_consonant = ''

    for ch in string:
        if ch in consonants:
            s_consonant = s_consonant + ch
        elif ch in vowels:
            s_vowel = s_vowel + ch

    print(s_vowel)
    print(s_consonant)
