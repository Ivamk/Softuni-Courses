original_numbers = input().split(", ")
final_numbers = []
for el in original_numbers:
    if int(el) == 0:
        original_numbers.remove(el)
        original_numbers.append('0')
for elem in original_numbers:
    final_numbers.append(int(elem))
print(final_numbers)
