name_of_product = input()
type = ' '
if name_of_product == 'banana' or name_of_product == 'apple' or name_of_product == 'kiwi' or name_of_product == 'cherry'\
        or name_of_product == 'lemon' or name_of_product == 'grapes':
    type = 'fruit'
elif name_of_product == 'tomato' or name_of_product == 'cucumber' or name_of_product == 'pepper' or name_of_product == 'carrot':
    type = 'vegetable'
else:
    type = 'unknown'
print(type)

