cap_first_number = int(input())
cap_second_number = int(input())
cap_third_number = int(input())
if_prime = False
if_first = False
if_third = False
for first in range(2, cap_first_number + 1):
    if_first = False
    if first % 2 == 0:
        if_first = True
    for second in range(2, cap_second_number + 1):
        if_prime = False
        if second == 2 or second == 3 or second == 5 or second == 7:
            if_prime = True
        for third in range(2, cap_third_number + 1):
            if_third = False
            if third % 2 == 0:
                if_third = True
            if if_prime and if_first and if_third:
                print(f'{first} {second} {third}')



