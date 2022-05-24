weight = int(input())
lenght = int(input())
total_pieces = weight * lenght
sum_pieces = 0
is_eaten = True
while sum_pieces <= total_pieces:
    pieces = input()
    if pieces == 'STOP':
        is_eaten = False
        break
    else:
        pieces = int(pieces)
        sum_pieces += pieces
difference = abs(total_pieces-sum_pieces)
if is_eaten:
    print(f'No more cake left! You need {difference} pieces more.')
else:
    print(f'{total_pieces - sum_pieces} pieces are left.')
