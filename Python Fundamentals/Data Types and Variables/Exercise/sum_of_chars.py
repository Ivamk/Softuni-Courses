n_number = int(input())
sum = 0
for seq in range(n_number):
    character = input()
    sum += ord(character)
print(f"The sum equals: {sum}")
