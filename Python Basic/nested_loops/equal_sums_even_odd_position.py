number_1 = int(input())
number_2 = int(input())

for num in range(number_1, number_2 + 1, 1):
    sum_odd = 0
    sum_even = 0
    number_to_str = str(num)
    for index, character in enumerate(number_to_str):
        if index % 2 == 0:
            sum_odd += int(character)
            # защото за комп започва индекса от 0 и е четно, а за нас е 1ва цифра и е нечетно
        else:
            sum_even += int(character)
    if sum_even == sum_odd:
        print(num, end=' ')
