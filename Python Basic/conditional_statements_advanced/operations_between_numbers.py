n1_number = int(input())
n2_number = int(input())
operator = input()
result = 0
if operator == '+':
    result = n1_number + n2_number
    if result % 2 == 0:
        print(f'{n1_number} {operator} {n2_number} = {result} - even')
    else:
        print(f'{n1_number} {operator} {n2_number} = {result} - odd')
elif operator == '-':
    result = n1_number - n2_number
    if result % 2 == 0:
        print(f'{n1_number} {operator} {n2_number} = {result} - even')
    else:
        print(f'{n1_number} {operator} {n2_number} = {result} - odd')
elif operator == '*':
    result = n1_number * n2_number
    if result % 2 == 0:
        print(f'{n1_number} {operator} {n2_number} = {result} - even')
    else:
        print(f'{n1_number} {operator} {n2_number} = {result} - odd')
elif operator == '/' and not n2_number == 0:
    result = n1_number / n2_number
    print(f'{n1_number} / {n2_number} = {result:.2f}')
elif operator == '%' and not n2_number == 0:
    result = n1_number % n2_number
    print(f'{n1_number} % {n2_number} = {result}')
elif (operator == '/' or operator == '%') and n2_number == 0:
    print(f'Cannot divide {n1_number} by zero')

