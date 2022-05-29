TANK_CAPACITY = 255
stage_full = 0
number_lines = int(input())
for i in range(number_lines):
    current_littres = int(input())
    if stage_full + current_littres > TANK_CAPACITY:
        print(f"Insufficient capacity!")

    else:
        stage_full += current_littres
print(stage_full)
