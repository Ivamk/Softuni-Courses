number = int(input())
sum_number_odd = 0
sum_number_even = 0
for sequence in range(1, number + 1):
    left_numbers = int(input())
    if sequence % 2 == 1:
        sum_number_odd += left_numbers
    else:
        sum_number_even +=left_numbers

difference = abs(sum_number_odd - sum_number_even)
if sum_number_odd == sum_number_even:
    print('Yes')
    print(f'Sum = {sum_number_odd}')
else:
    print('No')
    print(f'Diff = {difference}')


