number = int(input())
number_as_string = str(number)
sorted_number = sorted(number_as_string, reverse=True)

print(*sorted_number, sep="")
