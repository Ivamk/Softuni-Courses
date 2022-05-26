command = input()
number_coffee = 0
lowercase = ["coding", "dog", "cat", "movie"]
uppercase = ["CODING", "DOG", "CAT", "MOVIE"]
while not command == "END":
    if command in lowercase:
        number_coffee += 1
    elif command in uppercase:
        number_coffee += 2
    command = input()
if number_coffee <= 5:
    print(number_coffee)
else:
    print("You need extra sleep")

