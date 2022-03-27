'''---------------------------------------------------------------------
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
- The game can be played with N players [ ]
- If you capture a King (13), then all players must give you 4 extra
    cards. [ ]
- If you capture a Queen (12), then you must give all opponents 4 extra
    cards. [ ]
- If a King takes a Queen of the same suit, then that player wins. [ ]
------------------------------------------------------------------------'''

import itertools, random

class war_game:
    def __init__(self):
        deck = self.generate_deck()
        random.shuffle(deck)
        players = self.deal_cards(deck, 2)
        self.player_one, self.player_two = players[0], players[1]
        self.round_cards = []
        self.buffer = []
        self.round = 1
        self.players = players
        self.round_winner = None # Default winner of the round at start is no one

    def generate_deck(self):
        deck = list(itertools.product(range(2, 15), ['Spade', 'Heart', 'Diamond', 'Club']))
        return sorted(deck, key=lambda tup: tup[0])
    
    def generate_players(self, num_players):
        players = []
        for i in range(num_players):
            if i < 52: # Edge case where more players than cards are entered
                players.append(list())
            
        return players
    
    def deal_cards(self, deck, num_players):
        player_ID = 0 # Initialise player to be dealt to as Player 1, index 0
        players = self.generate_players(num_players)
        
        for card in deck:
            if player_ID == num_players:
                player_ID = 0 # Reset player to be dealt to
            
            players[player_ID].append(card)
            player_ID = player_ID + 1
            
        return players
    
    def compare_cards(self, card_a, card_b):
        if card_a[0] > card_b[0]:
            return 1
        if card_a[0] == card_b[0]:
            return 0
        if card_a[0] < card_b[0]:
            return -1
    
    def print_cards(self):
        for i in range(len(self.round_cards)):
            print("Player", i + 1, "draws", self.round_cards(i))

    def compare_cards(self):
        if self.all_cards_equal():
            return False # It's a tie

        battle = list()
        for i in range(len(self.round_cards)):
            battle.append((i, self.round_cards[i]))

        sorted_battle = sorted(battle, key=lambda tup: tup[1][0])
        winner_index = sorted_battle[-1][0]
        
        print("Player", winner_index + 1, "wins the round!")
        
        self.players[winner_index].extend(self.round_cards)
        self.players[winner_index].extend(self.buffer)
        self.buffer = []
        
        return True
        

    def all_cards_equal(self):
        value = iter([card[0] for card in self.round_cards])
        try:
            first = next(value)
        except StopIteration:
            return True
        return all(first == val for val in value)

    def play_round(self, num_players):
        if self.win_check() and num_players < 52: # Check for a winner
            return self.game_over()
        
        print("Round #" + str(self.round))
        
        for i in range(len(self.players)):
            self.round_cards.append(self.players[i].pop(0))
        
        self.print_cards()

        #card_one, card_two = self.player_one.pop(0), self.player_two.pop(0)
        #print("Player 1 plays", card_one, "face up.\tPlayer 2 plays", card_two, "face up.")
        battle_result = self.compare_cards(card_one, card_two)
        
        match battle_result:
            case 0: # Tie
                print("The round is a tie! Initialising tie breaker.")
                if self.win_check():
                    return self.game_over()
                
                if self.is_tie():
                    return self.tie_default()
                
                temp_buffer = list()
                for i in range(3):
                    for player in range(num_players):
                        if player == 0:
                            card = self.player_one.pop(0)
                        elif player == 1:
                            card = self.player_two.pop(0)

                        temp_buffer.append(card)
                
                print("Player 1 & 2 place three cards face down.")
                self.buffer.extend(temp_buffer)
                return self.play_round(num_players)
                
            case 1: # Player 1 wins the round
                print("Player 1 wins the round!")
                self.player_one.extend([card_one, card_two])
                self.player_one.extend(self.buffer)
                self.buffer = []
            case -1: # Player 2 wins the round
                print("Player 2 wins the round!")
                self.player_two.extend([card_one, card_two])
                self.player_two.extend(self.buffer)
                self.buffer = []
        
        self.round = self.round + 1 # Increment the round counter
        return True
    
    def is_tie(self):
        for player in self.players:
            if len(player) < 4:
                return True
        
    def tie_default(self):
        if len(self.player_two) < len(self.player_one):
            print("Player 2 does not have enough cards to tie break. Player 1 wins by default!")
        elif len(self.player_two) > len(self.player_one):
            print("Player 1 does not have enough cards to tie break. Player 2 wins by default!")
        else:
            print("It's a tie!")

        return False
    
    def win_check(self):
        if len(self.player_one) == 0 or len(self.player_two) == 0:
            return True
        
    def game_over(self):
        if len(self.player_two) == 0:
            if len(self.player_one) == 0:
                print("The game is a tie!")
            else:
                print("Player 1 wins the game!")
        else:
            print("Player 2 wins the game!")
            
        return False
    
if __name__ == '__main__':
    war_card_game = war_game()
    while war_card_game.play_round(2):
        continue