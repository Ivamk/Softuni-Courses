number_bottles = int(input())
command = input()
total_detergent = number_bottles * 750
needed_detergent = 0
row_refill = 0
number_plates_clean = 0
number_pans_clean = 0
detergent_is_finished = False
while command != 'End':
    number_plates = int(command)
    row_refill += 1
    if row_refill % 3 != 0:
        needed_detergent += number_plates * 5
        number_plates_clean += number_plates
    else:
        needed_detergent += number_plates * 15
        number_pans_clean += number_plates
    if needed_detergent > total_detergent:
        detergent_is_finished = True
        break
    command = input()
difference = abs(needed_detergent - total_detergent)
if detergent_is_finished:
    print(f"Not enough detergent, {difference} ml. more necessary!")
else:
    print(f'Detergent was enough!')
    print(f'{number_plates_clean} dishes and {number_pans_clean} pots were washed.')
    print(f"Leftover detergent {difference} ml.")
