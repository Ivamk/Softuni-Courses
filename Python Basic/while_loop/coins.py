change = float(input())
change_coins = int(change * 100)
sum_coins = 0
sum_coins += change_coins // 200
change_coins %= 200
sum_coins += change_coins // 100
change_coins %= 100
sum_coins += change_coins // 50
change_coins %= 50
sum_coins += change_coins // 20
change_coins %= 20
sum_coins += change_coins // 10
change_coins %= 10
sum_coins += change_coins // 5
change_coins %= 5
sum_coins += change_coins // 2
change_coins %= 2
if change_coins > 0:
    sum_coins += 1
print(sum_coins)
