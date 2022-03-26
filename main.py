
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
        
    def make_turn(players):
        if len(players) == 2:
            return warGame.base_turn(players)
        else:
            #return warGame.extended_turn(players)
            pass

    def base_turn(players):
        is_winner = False
        turn_counter = 0
        
        while is_winner == False:
            # Draw cards
            cards = []
            for player in players:
                cards[player] = warGame.get_card(players[player], 0)
                print("Player", player, "draws:", cards[player])
            
            # Compare cards
            comparison = warGame.compare_cards(cards[0], cards[1])
            
            # Determine win or tie
            match comparison:
                case 1: # Player 1 wins
                    players[1] = warGame.pop_card(players[1])
                    players[0] = warGame.add_card(players[0], cards[1])
                case 0: # Tie
                    buffer = [cards[0], cards[1]] # Generate buffer
                    index = 4 # Start index
                    
                    # Until tie broken
                    while comparion == 0:
                        tie_cards = [[], []] # Initialise tie cards
                        for player in players:
                            for i in range((index + 1) - 4, index + 1): # Draw four cards
                                tmp_card = warGame.get_card(players[player]), index
                                tie_cards[player].append(tmp_card)
                        
                        index = index + 4
                        comparison = warGame.compare_cards(tie_cards[0][3], tie_cards[1][3])
                        
                        
                case -1: # Player 2 wins
                    pass
            # If win delete & add cards respectively
            # If tie draw 4 cards, compare 4th card, then delete & add cards respectively
            # Check if either player has 0 cards, if yes say player x wins end loop.
            pass

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
    
