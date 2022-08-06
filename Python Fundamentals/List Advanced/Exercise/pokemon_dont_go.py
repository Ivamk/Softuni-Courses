def action(pokemon, deleted):
    for el in range(0, len(pokemon)):
        if pokemon[el] <= deleted:
            pokemon[el] += deleted
        else:
            pokemon[el] -= deleted
    return pokemon


distance_pokemon = [int(el) for el in input().split()]
sum_removed_pokemons = 0
index = int(input())
while not len(distance_pokemon) == 0:
    if index < 0:
        del_el = int(distance_pokemon.pop(0))
        distance_pokemon = distance_pokemon[::-1]
        distance_pokemon.append(distance_pokemon[0])
        distance_pokemon = distance_pokemon[::-1]
        distance_pokemon = action(distance_pokemon, del_el)
    elif index >= len (distance_pokemon):
        del_el = int(distance_pokemon.pop(-1))
        distance_pokemon.append(int(distance_pokemon[0]))
        distance_pokemon = action(distance_pokemon, del_el)
    else:
        del_el = int(distance_pokemon.pop(index))
        distance_pokemon = action(distance_pokemon, del_el)
    sum_removed_pokemons += del_el
    if len(distance_pokemon) == 0:
        break
    index = int(input())
print(sum_removed_pokemons)
