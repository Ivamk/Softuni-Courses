n = int(input())
word = input()
listche = []
second_listche = []
for _ in range(n):
    current_word = input()
    listche.append(current_word)
    if word in current_word:
        second_listche.append(current_word)
print(listche)
print(second_listche)
