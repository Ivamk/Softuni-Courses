def sorted_numbers(list_of):
    return sorted(list_of)


numbers = input().split()
numbers_int = []
for el in numbers:
    numbers_int.append((int(el)))
print(sorted_numbers(numbers_int))


