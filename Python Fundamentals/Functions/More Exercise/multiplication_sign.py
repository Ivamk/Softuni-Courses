number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

counter = 0
is_zero = False

if number_1 == 0 or number_2 == 0 or number_3 == 0:
    print("zero")
    is_zero = True
else:
    if number_1 < 0:
        counter += 1
    if number_2 < 0:
        counter += 1
    if number_3 < 0:
        counter += 1

if counter % 2 == 0 and is_zero is False:
    print("positive")
elif counter % 2 != 0 and is_zero is False:
    print("negative")
