some_string="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
x=3
for y in range(x, len(some_string)+x,x):
    res=some_string[y-x:y]
print(res)