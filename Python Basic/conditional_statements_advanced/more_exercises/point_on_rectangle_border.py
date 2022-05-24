# x1, y1, x2, y2, x и y

x1_abciss = float(input())
y1_ordinat = float(input())
x2_abciss = float(input())
y2_ordinat = float(input())
x_abciss = float(input())
y_ordinat = float(input())

result = ' '

if (x_abciss == x1_abciss or x_abciss == x2_abciss) and (y_ordinat > y1_ordinat and y_ordinat < y2_ordinat):
    result = "Border"
elif (y_ordinat == y1_ordinat or y_ordinat == y2_ordinat) and (x_abciss > x1_abciss and x_abciss < x2_abciss):
    result = "Border"
elif (x_abciss == x1_abciss or x_abciss == x2_abciss) and (y_ordinat == y1_ordinat or y_ordinat == y2_ordinat):
    result = "Border"
else:
    result = "Inside / Outside"

print(result)
