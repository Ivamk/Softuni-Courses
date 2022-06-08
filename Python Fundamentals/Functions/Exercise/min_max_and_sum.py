def function(list_of):
    return f"The minimum number is {min(list_of)}\nThe maximum number is {max(list_of)}\nThe sum number is: {sum(list_of)}"

numbers = input().split()
numbers_int = []
for el in numbers:
    numbers_int.append((int(el)))
print(function(numbers_int))
