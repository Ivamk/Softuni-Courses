number_combinations = int(input())
number1 = int(input())
number2 = int(input())

sum_numbers = number1 + number2
is_sum = True
difference = 0

for numbers in range(1, number_combinations):
    number1 = int(input())
    number2 = int(input())

    sum_numbers_previous = number1 + number2
    if sum_numbers == sum_numbers_previous:
        is_sum = True
    else:
        is_sum = False

        if sum_numbers > sum_numbers_previous:
            difference = sum_numbers - sum_numbers_previous
        else:
            difference = sum_numbers_previous - sum_numbers

    sum_numbers = number1 + number2

if is_sum:
    print(f"Yes, value={sum_numbers}")
else:
    print(f"No, maxdiff={difference}")