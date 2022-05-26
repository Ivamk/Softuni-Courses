word = input()
number_symbols = len(word)

for seq in range(number_symbols):
    letter = word[seq]
    print(letter*2, end='')

