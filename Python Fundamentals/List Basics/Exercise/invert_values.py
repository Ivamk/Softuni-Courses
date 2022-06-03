numbers = input().split(' ')
opposite_numbers = []
for index in range(len(numbers)):
    opposite_number = -int(numbers[index])
    opposite_numbers.append(opposite_number)
print(opposite_numbers)
