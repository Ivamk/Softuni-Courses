def order(name_product, quantity_sold):
    if name_product == "coffee":
        return quantity_sold * 1.5
    elif name_product == "coke":
        return quantity_sold * 1.4
    elif name_product == "water":
        return quantity_sold
    elif name_product == "snacks":
        return quantity_sold * 2


product = input()
quantity = int(input())

print(f"{order(product, quantity):.2f}")
