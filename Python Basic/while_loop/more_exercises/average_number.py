n_number = int(input())
sum_numbers = 0
for sequence in range(n_number):
    current_number = int(input())
    sum_numbers += current_number
average = sum_numbers / n_number
print(f'{average:.2f}')
