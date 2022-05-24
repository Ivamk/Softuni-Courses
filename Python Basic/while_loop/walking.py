goal_steps = 10000
sum_steps = 0
while sum_steps <= goal_steps:
    command = input()
    if command != 'Going home':
        current_steps = int(command)
        sum_steps += current_steps
    else:
        current_steps = int(input())
        sum_steps += current_steps
        break
difference = abs(sum_steps - goal_steps)
if sum_steps >= goal_steps:
    print(f'Goal reached! Good job!\n{difference} steps over the goal!')
else:
    print(f'{difference} more steps to reach goal.')


