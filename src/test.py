round_cards = [(3, 'Heart'), (4, 'Diamond'), (5, 'Club'), (6, 'Spade')]

'''battle = list()

for i in range(len(round_cards)):
    battle.append((i, round_cards[i]))

sorted_battle = sorted(battle, key=lambda tup: tup[1][0])
winner = sorted_battle[-1][0]
print(sorted_battle)
print(winner)'''

players = [(0, [(3, 'Heart'), (4, 'Diamond'), (5, 'Club'), (6, 'Spade')]), \
        (1, [(3, 'Heart'), (4, 'Diamond'), (5, 'Club'), (6, 'Spade')]), \
        (2, [(3, 'Heart'), (4, 'Diamond'), (5, 'Club'), (6, 'Spade')]), \
        (3, [(3, 'Heart'), (4, 'Diamond'), (5, 'Club'), (6, 'Spade')])]

players_eliminated = [2, 3]


def test(players, ID):
    print("Before:", players)
    for i in range(len(players)):
        if players[i][0] == ID:
            players.pop(i)
        break
            
    print("After:", players)
    return players
            
for player in players_eliminated:
    players = test(players, player)