number_n = int(input())

for current_number in range(1111, 10000):
    number_is_special = True
    current_number_as_string = str(current_number)  # превръщаме текущото четирицифрено число в string
    for current_digit in current_number_as_string:  # започваме да изпълняваме текущият цикъл за всеки символ в четирицифреното число
        if int(current_digit) == 0 or number_n % int(current_digit) != 0:   # и с този цикъл проверяваме дали в текущото число има 0 или остатък различен от 0
            number_is_special = False
            break
    if number_is_special:
        print(current_number, end=" ")
