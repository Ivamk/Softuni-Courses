companions_count = int(input())
days = int(input())
coins = 0
for i in range(1, days + 1):
    if i % 10 == 0:
        companions_count -= 2
    if i % 15 == 0:
        companions_count += 5
        coins -= companions_count * 2
    coins += (50 - companions_count * 2)
    if i % 3 == 0:
        coins -= companions_count * 3
    if i % 5 == 0:
        coins += companions_count * 20
if not companions_count == 0:
    coins_per_companion = coins // companions_count
    print(f"{companions_count} companions received {coins_per_companion} coins each.")
