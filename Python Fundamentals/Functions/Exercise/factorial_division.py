def factorial(first, second):
    for seq in range(1, first):
        first *= seq
    for seq in range(1, second):
        second *= seq
    division = first / second
    return(f"{division:.2f}")


first_number = int(input())
second_number = int (input())
print(factorial(first_number, second_number))
