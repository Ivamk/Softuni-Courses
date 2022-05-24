graduses = float(input())

whether_is = ' '

if 26.00 <= graduses <= 35.00:
    whether_is = 'Hot'
elif 20.1 <= graduses <= 25.9:
    whether_is = "Warm"
elif 15.00 <= graduses <= 20.00:
    whether_is = "Mild"
elif 12 <= graduses <= 14.9:
    whether_is = "Cool"
elif 5 <= graduses <= 11.9:
    whether_is = "Cold"
else:
    whether_is = "unknown"

print(whether_is)
