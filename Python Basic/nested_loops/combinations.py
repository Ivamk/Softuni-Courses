n_result = int(input())
sum_correct = 0
for x1 in range(n_result + 1):
    for x2 in range(n_result + 1):
        for x3 in range(n_result + 1):
            result = x3+x2+x1
            if result == n_result:
                sum_correct += 1
print(sum_correct)
