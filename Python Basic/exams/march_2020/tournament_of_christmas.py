number_days = int(input())
won_money = 0
day_win = 0
day_lost = 0
for days in range(number_days):
    sport = input()
    wins = 0
    lost = 0
    won_money_day = 0
    while sport != 'Finish':
        result = input()
        if result == 'win':
            wins += 1
            won_money_day += 20
        elif result == 'lose':
            lost += 1
        if sport == 'Finish':
            break
        sport = input()
    if wins > lost:
        won_money_day *= 1.1
        day_win += 1
    else:
        day_lost +=1
    won_money += won_money_day

if day_win > day_lost:
    won_money *= 1.2
    print(f'You won the tournament! Total raised money: {won_money:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {won_money:.2f}')
