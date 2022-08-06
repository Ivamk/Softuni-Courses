number_rooms = int(input())
is_enough = True
free_chairs_left = 0
for seq in range(1, number_rooms+1):
    chairs, vistors = input().split()
    number_visitors = int(vistors)
    if len(chairs) >= number_visitors:
        free_chairs_left += (len(chairs) - number_visitors)
    else:
        needed_chairs = number_visitors - len(chairs)
        is_enough = False
        print(f"{needed_chairs} more chairs needed in room {seq}")

if is_enough:
    print(f"Game On, {free_chairs_left} free chairs left")
