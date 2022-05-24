needed_money = float(input())
money_at_beginning = float(input())
days_counter = 0
days_spend_counter = 0
is_sum = True
while money_at_beginning < needed_money:
    action = input()
    money_difference = float(input())
    days_counter += 1
    if action == 'spend':
        days_spend_counter += 1
        if money_difference >= money_at_beginning:
            money_at_beginning = 0
        else:
            money_at_beginning -= money_difference
        if days_spend_counter == 5:
            is_sum = False
            break
    elif action == 'save':
        days_spend_counter = 0
        money_at_beginning += money_difference
if is_sum:
    print(f'You saved the money for {days_counter} days.')
else:
    print(f"You can't save the money.\n{days_counter}")
