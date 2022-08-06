version = [int(el) for el in input().split('.')]

if version[2] < 9:
    version[2] += 1
elif version[2] == 9:
    if version[1] < 9:
        version[2] = 0
        version[1] += 1
    else:
        version[2] = 0
        version[1] = 0
        version[0] += 1

print(*version, sep='.')

