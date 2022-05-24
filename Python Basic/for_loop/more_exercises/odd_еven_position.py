import sys

n_numbers = int(input())
odd_sum = 0
even_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_min = sys.maxsize
even_max = -sys.maxsize
for sequence in range(1, n_numbers + 1):
    current_number = float(input())
    if sequence % 2 == 1:
        odd_sum += current_number
        if current_number > odd_max:
            odd_max = current_number
        if current_number < odd_min:
            odd_min = current_number
    else:
        even_sum += current_number
        if current_number > even_max:
            even_max = current_number
        if current_number < even_min:
            even_min = current_number
print(f'OddSum={odd_sum:.2f},')
if odd_min == sys.maxsize:
    print('OddMin=No,')
else:
    print(f'OddMin={odd_min:.2f},')
if odd_max == -sys.maxsize:
    print('OddMax=No,')
else:
    print(f'OddMax={odd_max:.2f},')

print(f'EvenSum={even_sum:.2f},')
if even_min == sys.maxsize:
    print('EvenMin=No,')
else:
    print(f'EvenMin={even_min:.2f},')
if even_max == -sys.maxsize:
    print('EvenMax=No')
else:
    print(f'EvenMax={even_max:.2f}')


# if odd_max == -sys.maxsize and even_max == -sys.maxsize:
#     print(f"OddSum={odd_sum:.2f},\nOddMin=No,\nOddMax=No,\
#      \nEvenSum={even_sum:.2f},\nEvenMin=No,\nEvenMax=No")
# elif odd_max == -sys.maxsize:
#     print(f"OddSum={odd_sum:.2f},\nOddMin=No,\nOddMax=No,\
#      \nEvenSum={even_sum:.2f},\nEvenMin={even_min:.2f},\nEvenMax={even_max:.2f}")
# elif even_max == -sys.maxsize:
#     print(f"OddSum={odd_sum:.2f},\nOddMin={odd_min:.2f},\nOddMax={odd_max:.2f},\
#      \nEvenSum={even_sum:.2f},\nEvenMin=No,\nEvenMax=No")
# else:
#     print(f"OddSum={odd_sum:.2f},\nOddMin={odd_min:.2f},\nOddMax={odd_max:.2f},\
#      \nEvenSum={even_sum:.2f},\nEvenMin={even_min:.2f},\nEvenMax={even_max:.2f}")