price_skumria_kg = float(input())
price_caca_kg = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())

price_palamud_kg = price_skumria_kg * 1.6
price_safrid_kg = price_caca_kg * 1.8
price_midi_kg = 7.50

total_price = price_palamud_kg * palamud_kg + price_safrid_kg * safrid_kg + price_midi_kg * midi_kg

print(f'{total_price:.2f}')
