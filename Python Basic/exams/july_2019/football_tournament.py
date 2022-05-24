name = input()
number_matches = int(input())
count_wins = 0
count_even = 0
count_lost = 0
for sequence in range(number_matches):
    result = input()
    if result == 'W':
        count_wins += 1
    elif result == 'D':
        count_even += 1
    elif result == 'L':
        count_lost += 1
total_score = count_wins * 3 + count_even

if number_matches == 0:
    print(f"{name} hasn't played any games during this season.")
else:
    print(f"{name} has won {total_score} points during this season.")
    print(f"Total stats:")
    print(f"## W: {count_wins}")
    print(f"## D: {count_even}")
    print(f"## L: {count_lost}")
    print(f"Win rate: {count_wins / number_matches * 100:.2f}%")
