kilometres_distance = int(input())
period = input()

price_lowest = 0

if kilometres_distance < 20:
    if period == 'day':
        price_lowest = 0.70 + 0.79 * kilometres_distance
    else:
        price_lowest = 0.70 + 0.90 * kilometres_distance
elif kilometres_distance < 100:
    price_lowest = 0.09 * kilometres_distance
else:
    price_lowest = 0.06 * kilometres_distance

print(f'{price_lowest:.2f}')
