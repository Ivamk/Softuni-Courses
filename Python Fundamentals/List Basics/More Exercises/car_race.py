sequence_numbers = input().split(" ")
middle = len(sequence_numbers)//2
left_side = sequence_numbers[:middle]
right_side = sequence_numbers[len(sequence_numbers):middle:-1]
time_left = 0
time_right = 0
multiplier = 1
for num in left_side:
    time_left += int(num)
    if num == "0":
        time_left *= 0.8
for num in right_side:
    time_right += int(num)
    if num == "0":
        time_right *= 0.8
if time_left < time_right:
    print(f"The winner is left with total time: {time_left:.1f}")
elif time_left > time_right:
    print(f"The winner is right with total time: {time_right:.1f}")
