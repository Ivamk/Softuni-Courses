budget = int(input())
all_prices = 0
all_needed_bought = True
current_price = input()
while not current_price == "End":
    current_price = int(current_price)
    all_prices += current_price
    if budget - all_prices < 0:
        print(f"You went in overdraft!")
        all_needed_bought = False
        break
    current_price = input()

if all_needed_bought:
    print("You bought everything needed.")
