number = int(input())
sum_number_left = 0
sum_number_right = 0
for sequence in range(1, number + 1):
    left_numbers = int(input())
    sum_number_left += left_numbers
for sequence in range(1, number + 1):
    right_numbers = int(input())
    sum_number_right += right_numbers

difference = abs(sum_number_left - sum_number_right)
if sum_number_left == sum_number_right:
    print(f'Yes, sum = {sum_number_left}')
else:
    print(f'No, diff = {difference}')
