first_number = int(input())
next_number = int(input())
sum_numbers = next_number
while sum_numbers < first_number:
    next_number = int(input())
    sum_numbers += next_number

print(sum_numbers)
