number_films = int(input())
highest_rating = 0
lowest_rating = 0
total_rating = 0
best_film = ''
worst_film = ''
for sequence in range(number_films):
    name = input()
    current_rating = float(input())
    if sequence == 0:
        highest_rating = current_rating
        lowest_rating = current_rating
    if current_rating >= highest_rating:
        highest_rating = current_rating
        best_film = name
    if current_rating <= lowest_rating:
        lowest_rating = current_rating
        worst_film = name
    total_rating += current_rating
average_rating = total_rating / number_films
print(f'{best_film} is with highest rating: {highest_rating:.1f}')
print(f'{worst_film} is with lowest rating: {lowest_rating:.1f}')
print(f'Average rating: {average_rating:.1f}')

