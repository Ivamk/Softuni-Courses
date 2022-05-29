current_year = int(input())
while True:
    current_year += 1
    current_year_as_string = str(current_year)
    happy_year = True
    for test_position in range(len(current_year_as_string)):    #тестови цикъл чрез който се обхожда цифра по цифра
        test_digit = current_year_as_string[test_position]  #тази ст-ст, която се намира на тест позишън в годината, тоест връща индеса на съовтетната позиция
        for current_position in range(len(current_year_as_string)):  #с този цикъл ще се обхожда цикъла и ще проверява дали test digit се или не се повтаря с друга цифра
            if test_digit == current_year_as_string[current_position] and not current_position == test_position:
                happy_year = False
                break
    if happy_year:
        print(current_year_as_string)
        break
