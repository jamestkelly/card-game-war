'''
------------------------------------------------------------------------
Card Game War
Scenario by: Patrick, R.
Solution by: Jim, K.
------------------------------------------------------------------------
Game Rules & To Do
------------------------------------------------------------------------
Base Game Rules
- Two players [X]
- The cards are all dealt equally to each player [X]
- Each round, Player 1 lays a card down face up at the same time that
       Player 2 lays a card down face up. Whoever has the highest value
       card, wins both the round and both cards, i.e. winner takes both
       cards. [X]
- Winning cards are added to the bottom of the winner's deck. [X]
- Aces are considered "high", i.e. a value of 14. [X]
- If both cards are of equal value, then three cards are dealt from each
    hand face down. Then, one more card is dealt face up to 'war'. The
    winner takes all of the cards (the 4 dealt from their oponent). If
    this results in a tie, then the process is repeated again. [X]
- The player that runs out of cards first loses. [X]
------------------------------------------------------------------------
Extended Game Rules
- The game can be played with N players [X]
- If you capture a King (13), then all players must give you 4 extra
    cards. [ ]
- If you capture a Queen (12), then you must give all opponents 4 extra
    cards. [ ]
- If a King takes a Queen of the same suit, then that player wins. [ ]
------------------------------------------------------------------------
Additional Rule by Jim
- If the game exceeds `max_turns` then the player with the most cards
    wins. [ ]
------------------------------------------------------------------------
'''

import itertools, random

class war_game:
    def __init__(self):
        self.num_players = 4
        deck = self.generate_deck()
        random.shuffle(deck)
        self.players = self.deal_cards(deck)
        self.round_cards = []
        self.round_players = []
        self.buffer = []
        self.round = 1
        self.round_winner = None # Default winner of the round at start is no one

    def generate_deck(self):
        deck = list(itertools.product(range(2, 15), ['Spade', 'Heart', 'Diamond', 'Club']))
        return sorted(deck, key=lambda tup: tup[0])
    
    def generate_players(self):
        players = []
        for i in range(self.num_players):
            if i < 52: # Edge case where more players than cards are entered
                players.append((i, list()))
            
        return players
    
    def deal_cards(self, deck):
        player_ID = 0 # Initialise player to be dealt to as Player 1, index 0
        players = self.generate_players()
        
        for card in deck:
            if player_ID == self.num_players:
                player_ID = 0 # Reset player to be dealt to
            
            players[player_ID][1].append(card)
            player_ID = player_ID + 1
            
        return players

    def print_cards(self):
        for i in range(len(self.round_cards)):
            print("Player", i, "draws", self.round_cards[i])

    def compare_cards(self):
        if self.all_cards_equal():
            return False # It's a tie

        battle = list()
        for i in range(len(self.round_cards)):
            battle.append((self.round_players[i], self.round_cards[i]))

        sorted_battle = sorted(battle, key=lambda tup: tup[1][0])
        winner_index = sorted_battle[-1][0]
        print("Player", winner_index + 1, "wins the round!")
        self.players[winner_index][1].extend(self.round_cards)
        self.players[winner_index][1].extend(self.buffer)
        self.buffer = []
        self.round_players = []
        self.round_cards = []
        
        return True

    def all_cards_equal(self):
        value = iter([card[0] for card in self.round_cards])
        try:
            first = next(value)
        except StopIteration:
            return True
        return all(first == val for val in value)
    
    def remove_player(self, player_id):
        for i in range(len(self.players)):
            if self.players[i][0] == player_id:
                self.players.pop(i)
            break
    
    def eliminate_players(self):
        check = 0
        for i in range(len(self.players)):
            if len(self.players[i][1]) != 0 and self.players[i][1] != []:
                check = check + 1
        
        if check > 1:
            players_eliminated = []
            for i in range(len(self.players)):
                if len(self.players[i][1]) == 0:
                    print("Player", i, "was eliminated!")
                    players_eliminated.append(i)
                    
            for loser in players_eliminated:
                self.remove_player(loser)
                    
    def play_round(self):
        self.eliminate_players()
        if self.win_check() and self.num_players < 52: # Check for a winner
            return self.game_over()
        
        print("Round #" + str(self.round))
        
        for i in range(len(self.players)):
            if len(self.players[i][1]) >= 1:
                self.round_cards.append(self.players[i][1].pop(0))
                self.round_players.append(i)
        
        self.print_cards()
        battle_result = self.compare_cards()

        if (battle_result != True):
            print("The round is a tie!")
            if self.win_check():
                return self.game_over()
            
            if self.is_too_few_cards():
                return self.tie_default()
            
            return self.play_round()

        self.round = self.round + 1 # Increment the round counter
        return True
    
    def tie_breaker(self):
        for i in range(3):
            for j in range(len(self.players)):
                if self.players[j][1] != None:
                    card = self.players[j][1].pop(0)
                    self.buffer.append(card)
    
    def is_too_few_cards(self):
        for player in self.players:
            if len(player[1]) < 4:
                return True
        
    def tie_default(self):
        for i in range(len(self.players)):
            if len(self.players[i][1]) < 4:
                print("Player", self.players[i][0], "does not have enough" \
                        + " cards to continue, they have been eliminated.")
                for j in range(len(self.players[i][1])):
                    self.buffer.append(self.players[i][1][j])
                    
                self.players.pop(i)
        
        return False
    
    def win_check(self):
        player_count = 0
        for i in range(len(self.players)):
            if len(self.players[i][1]) >= 1:
                player_count = player_count + 1
                
        if player_count == 1:
            return True
        else:
            return False
        
    def game_over(self):
        for i in range(len(self.players)):
            if len(self.players[i][1]) >= 1:
                print("Player", self.players[i][0], "wins!")
                return False
            
        print("The game is a tie!")
        
        return False
    
if __name__ == '__main__':
    
    war_card_game = war_game()
    while war_card_game.play_round():
        continue