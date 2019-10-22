limit = int(input())
first_match = 0
second_match = 0
result = []
for i in range(1, limit + 1):
    first_match = input().split()
    ban_score_first_match = sum(map(int, first_match[:2]))
    pak_score_first_match = sum(map(int, first_match[2:]))
    second_match = input().split()
    ban_score_second_match = sum(map(int, second_match[:2]))
    pak_score_second_match = sum(map(int, second_match[2:]))
    if (ban_score_first_match > pak_score_first_match) and (ban_score_second_match > pak_score_second_match):
        result.append("Banglawash")
    else:
        result.append("Miss")
print('\n'.join(result))
