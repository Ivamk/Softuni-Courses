command = input()
total_tickets = 0
students_counter = 0
standard_counter = 0
kids_counter = 0

while command != 'Finish':
    movie_name = command
    free_spaces = int(input())
    total_places = free_spaces
    sold_tickets = 0
    while free_spaces > 0:
        type_tickets = input()
        if type_tickets == 'End':
            break
        elif type_tickets == 'standard':
            standard_counter += 1
        elif type_tickets == 'kid':
            kids_counter += 1
        elif type_tickets == 'student':
            students_counter += 1
        total_tickets += 1
        free_spaces -= 1
        sold_tickets += 1
    percentage_full_movie = sold_tickets / total_places * 100
    print(f'{movie_name} - {percentage_full_movie:.2f}% full.')
    command = input()
percentage_students = students_counter / total_tickets * 100
percentage_kids = kids_counter / total_tickets * 100
percentage_standard = standard_counter / total_tickets * 100
print(f'Total tickets: {total_tickets}')
print(f"{percentage_students:.2f}% student tickets.")
print(f'{percentage_standard:.2f}% standard tickets.')
print(f'{percentage_kids:.2f}% kids tickets.')
