start_num = int(input())
end_num = int(input())
magic_num = int(input())
first = 0
second = 0
sum_combinations = 0
if_found = False
for first_num in range(start_num, end_num + 1):
    for second_num in range(start_num, end_num + 1):
        result = first_num + second_num
        sum_combinations += 1
        if result == magic_num:
            first = first_num
            second = second_num
            if_found = True
            break
    if result == magic_num:
        break
if if_found:
    print(f'Combination N:{sum_combinations} ({first} + {second} = {magic_num})')
else:
    print(f'{sum_combinations} combinations - neither equals {magic_num}')
