population = [int(el) for el in input().split(", ")]
minimum_health = int(input())
if sum(population) / len(population) < minimum_health:
    print("No equal distribution possible")
else:
    for i in range(len(population)):
        if population[i] < minimum_health:
            diff = minimum_health - population[i]
            population[i] = minimum_health
            max_index = population.index(max(population))
            population[max_index] -= diff
    print(population)