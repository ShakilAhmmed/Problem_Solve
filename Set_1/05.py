sentence = input()
for change in sentence:
    if change in ['w', 'W']:
        print(sentence.replace(change, '#'))
