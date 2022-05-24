command = input()
sum_all_install = 0
while command != "NoMoreMoney":
    current_sum = float(command)
    if current_sum < 0:
        print('Invalid operation!')
        break
    sum_all_install += current_sum
    print(f'Increase: {current_sum:.2f}')
    command = input()
print(f'Total: {sum_all_install:.2f}')
