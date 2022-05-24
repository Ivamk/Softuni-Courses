lenght = int(input())
wight = int(input())
height = int(input())
percentage = float(input())

volume = lenght * wight * height

volume_left_cm = volume * (1 - percentage / 100)

volume_left_dm = volume_left_cm / 1000

water_needed_littres = volume_left_dm

print(water_needed_littres)
