value_voucher = int(input())
purchase = input()
count_tickets = 0
count_other = 0
while purchase != 'End':
    price = 0
    is_film = True
    if len(purchase) >= 8:
        price = ord(purchase[0]) + ord(purchase[1])
    else:
        is_film = False
        price = ord(purchase[0])
    value_voucher -= price
    if value_voucher < 0:
        break
    if is_film:
        count_tickets += 1
    else:
        count_other += 1
    purchase = input()
print(f'{count_tickets}')
print(f'{count_other}')
