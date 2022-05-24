name_favourite_book = input()
current_book = input()
sum_books = 0
is_founded = True
while current_book != name_favourite_book:
    if current_book == "No More Books":
        is_founded = False
        break
    else:
        sum_books += 1
        current_book = input()
if is_founded:
    print(f'You checked {sum_books} books and found it.')
else:
    print(f'The book you search is not here!\nYou checked {sum_books} books.')
