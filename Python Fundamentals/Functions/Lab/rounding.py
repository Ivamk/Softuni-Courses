num_as_string = input().split()
rounded_nums = []
for el in num_as_string:
    rounded_nums.append(round(float(el)))

print(rounded_nums)
