name_animal = input()

type_of_the_animal = ' '

if name_animal == 'dog':
    type_of_the_animal = 'mammal'
elif name_animal == 'crocodile' or name_animal == 'tortoise' or name_animal == 'snake':
    type_of_the_animal = 'reptile'
else:
    type_of_the_animal = 'unknown'
print(type_of_the_animal)



