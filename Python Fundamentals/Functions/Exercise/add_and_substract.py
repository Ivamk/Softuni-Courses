def function(number_1, number_2):
    return number_1 + number_2


def substract(sum, number_3):
    return  sum - number_3


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
sum_of = function(num_1, num_2)
result = substract(sum_of, num_3)
print(result)
