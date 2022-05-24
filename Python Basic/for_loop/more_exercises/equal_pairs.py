import sys

number_combinations = int(input())
number1 = int(input())
number2 = int(input())
sum_numbers = number1 + number2
is_sum = True
difference = 0
max_difference = -sys.maxsize
for numbers in range(1, number_combinations):
    number1 = int(input())
    number2 = int(input())
    sum_numbers_next = number1 + number2
    if sum_numbers == sum_numbers_next:
        is_sum = True
    else:
        is_sum = False
        difference = abs(sum_numbers - sum_numbers_next)
        if difference > max_difference:
            max_difference = difference
    sum_numbers = number1 + number2
if is_sum:
    print(f"Yes, value={sum_numbers}")
else:
    print(f"No, maxdiff={max_difference}")
