import random

budget = int(input("Въведи сума, кратна на 10, която ще залагаш: "))
your_bet = int(input("Въведи твоето предположение - число между 2 и 12: "))

while True:
    first_dice = random.randint(1, 6)
    second_dice = random.randint(1, 6)
    computer_bet = first_dice + second_dice
    print(f"Резултатът от хвърлянето на зарове е: {computer_bet}")

    if your_bet == computer_bet:
        budget += 50
        print("Поздравления, ти спечели 50 лева")

    else:
        budget -= 10
        print("Ти загуби 10 лева")

    if budget > 0:
        print(f"Твоят бюджет е: {budget}")
        print("Искаш ли да продължиш?")
        answer = input("Въведи Да/Не: ")
        print()
        if answer == "Да":
            your_bet = int(input("Въведи твоето предположение - число между 2 и 12: "))
            continue
        elif answer == "Не":
            print("Заповядай отново!")
            break
    else:
        print("Ти загуби всичките си пари!")
        break
