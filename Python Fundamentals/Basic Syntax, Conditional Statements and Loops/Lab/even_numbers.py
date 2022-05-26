n_number = int(input())
all_numbers_even = True
for seq in range(n_number):
    diff_number = int(input())
    if diff_number % 2 != 0:
        print(f"{diff_number} is odd!")
        all_numbers_even = False
        break
    else:
        continue
if all_numbers_even:
    print(f"All numbers are even.")
