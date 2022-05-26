animal_row = input().split(", ")
if animal_row[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    animal_row_reverse = animal_row[::-1]
    for seq in range(len(animal_row)):
        if animal_row_reverse[seq] == "wolf":
            print(f"Oi! Sheep number {seq}! You are about to be eaten by a wolf!")
