def digits(number):
    str_digits = str(number)
    even_sum = 0
    odd_sum = 0
    for el in str_digits:
        if int(el) % 2 == 0:
            even_sum += int(el)
        else:
            odd_sum += int(el)
    return(f"Odd sum = {odd_sum}, Even sum = {even_sum}")

single_number = int(input())
print(digits(single_number))
