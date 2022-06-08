def perfect(perfect_number):
    sum_divisors = 0
    for seq in range(1, perfect_number):
        if perfect_number % seq == 0:
            sum_divisors += seq
    if perfect_number == sum_divisors:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


perfect_number = int(input())
perfect(perfect_number)
