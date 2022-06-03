team_a = []
team_b = []
sent_out = input().split(" ")
game_over = False
for i in range(1, 12):
    team_a.append(f"A-{i}")
    team_b.append(f"B-{i}")
# for index in range(len(sent_out)):
#     if sent_out[index] in team_a:
#         team_a.remove(sent_out[index])
#     elif sent_out[index] in team_b:
#         team_b.remove(sent_out[index])
for player in sent_out:
    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)
    if len(team_a) < 7 or len(team_b) < 7:
        game_over = True
        break
print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if game_over:
    print("Game was terminated")
