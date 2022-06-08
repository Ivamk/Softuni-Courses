def collected(first, last):
    new_list = []
    for el in range(ord(first)+1, ord(last)):
        new_list.append(chr(el))
    return new_list


first_number = input()
second_number = input()
result = collected(first_number, second_number)
print(' '.join(result))
