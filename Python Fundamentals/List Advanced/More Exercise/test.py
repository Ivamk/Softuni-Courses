# 1=2#3=4#5=6

lst = input().split("#")
lst_first = []
for el in lst:
    lst_first.append(el.split("="))
print(lst_first)