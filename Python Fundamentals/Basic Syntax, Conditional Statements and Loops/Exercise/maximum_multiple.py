divisor = int(input())
boundary = int(input())
largest_number = 0
number = 0
while number <= boundary:
    if divisor == 0:
        break
    if number % divisor == 0:
        if number > largest_number:
            largest_number = number
    number +=1
print(f'{largest_number}')
