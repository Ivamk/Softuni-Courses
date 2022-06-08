# numbers = input().split()
# number_as_digit = []
# for el in numbers:
#     number_as_digit.append(int(el))
# is_even = lambda x: x % 2 == 0
# result = list(filter(is_even, number_as_digit))
#
# print(result)

def is_even(number):
    if number % 2 == 0:
        return True
    return False


numbers = input().split()
filtered_numbers = []
for el in numbers:
    if is_even(int(el)):
        filtered_numbers.append(int(el))
print(filtered_numbers)
