number_sequence = [int(el) for el in input().split()]
sentence = input()
num = []
new_word = []
for el in number_sequence:
    sum = 0
    for digit in str(el):
        sum += int(digit)
    num.append(sum)
for numbers in num:
    if numbers >= len(sentence):
        numbers = numbers - len(sentence)
        new_word.append(sentence[numbers])
        sentence = sentence[:numbers] + sentence[numbers + 1:]
    else:
        new_word.append(sentence[numbers])
        sentence = sentence[:numbers] + sentence[numbers + 1:]
print(*new_word, sep='')
