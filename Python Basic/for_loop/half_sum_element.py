import sys

number = int(input())
max_number = -sys.maxsize
sum_all_numbers = 0
for sequence in range(number):
    current_number = int(input())
    sum_all_numbers += current_number
    if current_number > max_number:
        max_number = current_number
if max_number == sum_all_numbers - max_number:
    print('Yes')
    print(f'Sum = {max_number}')
else:
    difference = abs(max_number - (sum_all_numbers - max_number))
    print('No')
    print(f'Diff = {difference}')


# Втори вариант без използване на sys.maxsize
# number = int(input())
# max_number = ' '              така казваме, че максималната стойност е str
# sum_all_numbers = 0
# for sequence in range(number):
#     current_number = int(input())
#     if sequence == 0:
#         max_number = current_number               така променяме стойността от стр на инт и след това вече може да сравняваме
#     if current_number > max_number:
#         max_number = current_number
