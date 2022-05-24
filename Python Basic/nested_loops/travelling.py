destination = input()
while destination != 'End':
    budget = float(input())
    savings = 0
    while savings < budget:
        save_money = float(input())
        savings += save_money
        if savings >= budget:
            print(f'Going to {destination}!')
    destination = input()



