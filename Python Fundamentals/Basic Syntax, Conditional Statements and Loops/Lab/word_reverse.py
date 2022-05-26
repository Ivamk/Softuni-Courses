word = input()
reverse_word = ''
for seq in range(len(word)-1, -1, -1):
    reverse_word += word[seq]
print(reverse_word)
