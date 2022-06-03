price_list = input().split(', ')
count_of_beggars = int(input())
new_list = []
count = 0
temp_sum = 0
while count < count_of_beggars:
    for el in range(count, len(price_list), count_of_beggars):
        temp_sum += int(price_list[el])
    new_list.append(temp_sum)
    temp_sum = 0
    count += 1
print(new_list)
