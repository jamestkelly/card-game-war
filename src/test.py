round_cards = [(3, 'Heart'), (4, 'Diamond'), (5, 'Club'), (6, 'Spade')]

battle = list()

for i in range(len(round_cards)):
    battle.append((i, round_cards[i]))

sorted_battle = sorted(battle, key=lambda tup: tup[1][0])
winner = sorted_battle[-1][0]
print(sorted_battle)
print(winner)