cards = input().split()
count_shuffles = int(input())
first_half = []
second_half = []
lenght_half = int(len(cards)/2)
for i in range(count_shuffles):
    final_deck = []
    first_half = cards[:lenght_half]
    second_half = cards[lenght_half:]
    for index in range(len(first_half)):
        final_deck.append(first_half[index])
        final_deck.append(second_half[index])
        cards = final_deck
print(final_deck)



