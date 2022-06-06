first_row = input().split()
second_row = input().split()
third_row = input().split()

conc_row = first_row + second_row + third_row
conc_row_int = [int(el) for el in conc_row]

is_draw = True
is_first = False
is_second = False
count_first = 0
count_second = 0
for seq in conc_row_int:
    if seq == 1:
        count_first += 1
        is_first = True
        if is_second == True:
            count_second = 0
            is_second = False
        if count_first == 3:
            print ("First player won")
            is_draw = False
            break
    elif seq == 2:
        count_second += 1
        is_second = True
        if is_first == True:
            count_first = 0
            is_first = False
        if count_second == 3:
            print("Second player won")
            is_draw = False
            break
    elif seq == 0:
        continue
if is_draw:
    print("Draw!")





