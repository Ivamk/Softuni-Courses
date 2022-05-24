needed_sum = int(input())
command = input()
counter = 0
cash_transactions = 0
card_transactions = 0
sum_donated = 0
people_cash = 0
people_card = 0
collected_money = False
while command != 'End':
    money = int(command)
    counter += 1
    if counter % 2 != 0:
        if money > 100:
            print('Error in transaction!')
        else:
            print('Product sold!')
            people_cash += 1
            sum_donated += money
            cash_transactions += money
    else:
        if money < 10:
            print('Error in transaction!')
        else:
            print('Product sold!')
            people_card += 1
            sum_donated += money
            card_transactions += money
    if needed_sum <= sum_donated:
        collected_money = True
        break
    command = input()
if collected_money:
    average_cs = cash_transactions / people_cash
    average_cc = card_transactions / people_card
    print(f'Average CS: {average_cs:.2f}')
    print(f"Average CC: {average_cc:.2f}")
else:
    print(f'Failed to collect required money for charity.')