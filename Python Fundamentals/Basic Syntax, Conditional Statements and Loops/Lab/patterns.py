number = int(input())
pattern = '*'
for seq in range(1, number + 1):
    print(pattern * seq)
for seq2 in range(number - 1, 0, -1):
    print(pattern * seq2)
