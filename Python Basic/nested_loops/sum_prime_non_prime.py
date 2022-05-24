number = input()
prime_numbers_sum = 0
nonprime_numbers_sum = 0
if_prime = False
while number != 'stop':
    num = int(number)
    if_prime = False
    if num < 0:
        print(f'Number is negative.')
        number = input()
        continue
    for i in range(2, num):
        if num % i == 0:
            if_prime = True
            break
    if if_prime:
        nonprime_numbers_sum += num
    else:
        prime_numbers_sum += num
    number = input()
print(f'Sum of all prime numbers is: {prime_numbers_sum}')
print(f'Sum of all non prime numbers is: {nonprime_numbers_sum}')