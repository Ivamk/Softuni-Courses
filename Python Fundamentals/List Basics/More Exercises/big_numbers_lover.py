# original_numbers = input().split(" ")
# integer_numbers = []
# for el in original_numbers:
#     integer_numbers.append(int(el))
# integer_numbers.sort(reverse=True)
#
# for element in integer_numbers:
#     print(element, end='')

numbers = input().split()
numbers.sort(reverse=True)
print(''.join(numbers))