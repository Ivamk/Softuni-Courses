# •	Баскетболни кецове – цената им е 40% по-малка от таксата за една година
# •	Баскетболен екип – цената му е 20% по-евтина от тази на кецовете
# •	Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип
# •	Баскетболни аксесоари – цената им е 1 / 5 от цената на баскетболната топка

yearly_tax_training = int(input())

sneakers = yearly_tax_training * 0.6
equipment = sneakers * 0.8
ball = equipment * 0.25
accessories = ball * 0.2

total_expenses = yearly_tax_training + sneakers + equipment + ball + accessories

print(total_expenses)