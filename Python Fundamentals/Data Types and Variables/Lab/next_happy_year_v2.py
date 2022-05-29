current_year = int(input())
while True:
    current_year += 1
    current_year_as_string = str(current_year)
    if len(current_year_as_string) == len(set(current_year_as_string)):   #set връща само уникални символа които са вътре в този стринг, а len(set...) връща колко уникални символа има
        print(current_year_as_string)
        break
