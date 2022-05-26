word = input()
new_letter = ""
while not word == "End":
    if word == "SoftUni":
        word = input()
        continue
    number_symbols = len(word)
    new_letter = ""
    for seq in range(number_symbols):
        letter = word[seq]
        new_letter += 2*letter
    print(new_letter)

    word = input()

