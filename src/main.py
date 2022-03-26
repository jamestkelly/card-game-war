# ------------------------------------------------------------------------
# Card Game War
# Scenario by: Patrick, R.
# Solution by: Jim, K.
# ------------------------------------------------------------------------
# Instructions & To Do
# ------------------------------------------------------------------------
# Original Game
# - Two players [X]
# - The cards are all dealt equally to each player [X]
# - Each round, Player 1 lays a card down face up at the same time that
#       Player 2 lays a card down face up. Whoever has the highest value
#       card, wins both the round and both cards, i.e. winner takes both
#       cards. [ ]
# - Winning cards are added to the bottom of the winner's deck. [ ]
# - Aces are considered "high", i.e. a value of 14. [X]
# - If both cards are of equal value, then three cards are dealt from each
#       hand face down. Then, one more card is dealt face up to 'war'. The
#       winner takes all of the cards (the 4 dealt from their oponent). If
#       this results in a tie, then the process is repeated again. [ ]
# - The player that runs out of cards first loses. [ ]
# ------------------------------------------------------------------------
# Extended Game | Additional Rules
# - The game can be played with N players [X]
# - If you capture a King (13), then all players must give you 4 extra
#       cards. [ ]
# - If you capture a Queen (12), then you must give all opponents 4 extra
#       cards. [ ]
# - If a King takes a Queen of the same suit, then that player wins. [ ]

import itertools, random

class warGame:
    def __init__(self):
        self.play_round(2)

    def play_round(num_players):
        deck = warGame.shuffle_deck(warGame.initialise_deck())
        players = warGame.deal(deck, warGame.initialise_players(num_players))
        return warGame.make_turn(num_players, players)
        
    def make_turn(num_players, players):
        if num_players == 2:
            warGame.base_turn(players)
            return True
        else:
            #return warGame.extended_turn(players)
            pass

    def base_turn(players):
        is_winner = False
        round_counter = 1
        
        while is_winner == False:
            print("Begin round", round_counter)
            cards = [] # Initialise cards array
            
            # Draw cards
            for player in players:
                cards[player] = warGame.get_card(players[player], 0)
                players[player] = warGame.pop_card(players[player])
                print("Player", player, "draws:", cards[player])
            
            # Compare cards
            comparison = warGame.compare_cards(cards[0], cards[1])
            
            # Determine win or tie
            match comparison:
                case 1: # Player 1 wins
                    players[0] = warGame.player_winner(0, cards, players)
                    print("Player 1 wins round", round_counter, ".")
                case -1: # Player 2 wins
                    players[1] = warGame.player_winner(1, cards, players)
                    print("Player 2 wins round", round_counter, ".")
                case 0: # Tie
                    print("It's a tie! Initialising tie breaker.")
                    is_winner = warGame.tie_breaker_check(players) # Check both players have enough cards
                    
                    buffer = warGame.initialise_buffer()
                    index = 4 # Start index
                    
                    # Until tie broken
                    while comparison == 0:
                        tie_cards = [[], []] # Initialise tie cards
                        for player in players:
                            for i in range(4): # Draw four cards
                                tmp_card = warGame.get_card(players[player], 0)
                                players[player] = warGame.pop_card(players[player])
                                tie_cards[player].append(tmp_card)
                        
                        temp_compare = warGame.compare_cards(tie_cards[0][3], tie_cards[1][3])
                        buffer = warGame.buffer_helper(tie_cards, buffer)
                        
                        if temp_compare == 1:
                            players = warGame.tie_winner(0, buffer, players)
                            comparison = temp_compare
                        if temp_compare == -1:
                            players = warGame.tie_winner(1, buffer, players)
                            comparison = temp_compare

            # Check if either player has 0 cards, if yes say player x wins end loop.
            is_winner = warGame.check_winner(players)
            
        return players
    
    def initialise_buffer(cards):
        buffer = [[], []]
        
        for card in cards:
            buffer[card].append(cards[card])
            
        return buffer
    
    def player_winner(winner, cards, players):
        for card in cards:
            players[winner].append(card)
            
        return players
    
    def tie_winner(winner, buffer, players):
        print("Player", winner, "wins the tie breaker!")
        for player in players:
            if player == winner:
                for i in len(buffer):
                    for j in len(buffer[player]):
                        players[player].append(buffer[player][j])
                        
        return players
    
    def tie_breaker_check(players):
        loser = None
        
        for player in players:
            if len(player) < 4:
                loser = player
        
        if loser == 0:
            print("Player 1 does not have enough cards to tie break.\n \
                  Player 2 wins!")
        elif loser == 1:
            print("Player 2 does not have enough cards to tie break.\n \
                  Player 1 wins!")
        else:
            return False
            
        return True
    
    def buffer_helper(tie_cards, buffer):
        for player in buffer:
            for card in tie_cards[player]:
                buffer[player].append(card)
                
        return buffer
                

    def check_winner(players):
        for player in players:
            if len(player) == 0:
                print(player + 1, "wins!")
                return True
            
        return False

    def compare_cards(card_a, card_b):
        if card_a > card_b:
            return 1
        if card_a == card_b:
            return 0
        if card_a < card_b:
            return -1
        
    def initialise_deck():
        return list(itertools.product(range(2, 15), ['Club', 'Diamond', 'Heart', 'Spade']))
    
    def shuffle_deck(deck):
        return random.sample(deck, len(deck))
        
    def get_card(deck, card_index):
        return deck[card_index]

    def deal(deck, players):
        max_cards = 52
        player_count = 0
        
        for card_index in range(max_cards):
            if player_count == len(players):
                player_count = 0
            
            current_card = warGame.get_card(deck, card_index)
            players[player_count].append(current_card)
            player_count = player_count + 1
            
        return players

    def initialise_players(num_players):
        player_list = []
        for player in range(num_players):
            player_list.append(list())
            
        return player_list
    
    def pop_card(player):
        if len(player) > 0:
            player.pop(0)
            
        return player
    
    def add_card(player, card):
        player.append(card)
        return player
    
if __name__ == 'main':
    game_over = False
    WG = warGame()
    
    while WG.play_round != True:
        continue