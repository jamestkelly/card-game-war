from random import shuffle
from main import *

wg = war_game() # Initialise the class

def test_generate_deck():
    assert len(wg.generate_deck()) == 52
    
def test_shuffle_deck():
    deck = wg.generate_deck()
    deck2 = wg.generate_deck()
    random.shuffle(deck2)
    assert deck != deck2

def test_generate_players():
    assert len(wg.generate_players(2)) == 2
    assert len(wg.generate_players(999)) == 52
    assert len(wg.generate_players(0)) == 0

def test_deal_cards():
    deck = wg.generate_deck()
    random.shuffle(deck)
    players = wg.deal_cards(deck, 2)
    assert len(players[0]) == 52 / 2
    assert len(players[1]) == 52 / 2

def test_compare_cards():
    assert wg.compare_cards((3, 'Heart'), (2, 'Spade')) == 1
    assert wg.compare_cards((2, 'Spade'), (2, 'Club')) == 0
    assert wg.compare_cards((2, 'Spade'), (3, 'Diamond')) == -1
    
def test_is_tie():
    player_one = [(3, 'Heart'), (4, 'Heart'), (5, 'Heart'), (6, 'Heart'), (7, 'Heart')]
    player_two = [(3, 'Heart'), (4, 'Heart'), (5, 'Heart'), (6, 'Heart'), (7, 'Heart')]
    wg.players = [player_one, player_two]
    assert wg.is_tie() == None
    
    player_one = [(3, 'Heart'), (4, 'Heart')]
    player_two = [(3, 'Heart'), (4, 'Heart')]
    wg.players = [player_one, player_two]
    assert wg.is_tie() == True
    
    player_one = [(3, 'Heart'), (4, 'Heart'), (5, 'Heart'), (6, 'Heart'), (7, 'Heart')]
    player_two = [(3, 'Heart'), (4, 'Heart')]
    wg.players = [player_one, player_two]
    assert wg.is_tie() == True
    
    player_one = [(3, 'Heart'), (4, 'Heart')]
    player_two = [(3, 'Heart'), (4, 'Heart'), (5, 'Heart'), (6, 'Heart'), (7, 'Heart')]
    wg.players = [player_one, player_two]
    assert wg.is_tie() == True
    
def test_tie_default():
    wg.player_one = [(3, 'Heart'), (4, 'Heart')]
    wg.player_two = [(3, 'Heart'), (4, 'Heart')]
    assert wg.tie_default() == False
    
    wg.player_one = [(3, 'Heart'), (4, 'Heart'), (5, 'Heart'), (6, 'Heart'), (7, 'Heart')]
    wg.player_two = [(3, 'Heart'), (4, 'Heart')]
    assert wg.tie_default() == False
    
    wg.player_one = [(3, 'Heart'), (4, 'Heart')]
    wg.player_two = [(3, 'Heart'), (4, 'Heart'), (5, 'Heart'), (6, 'Heart'), (7, 'Heart')]
    assert wg.tie_default() == False
    
def test_win_check():
    wg.player_one = [(3, 'Heart'), (4, 'Heart')]
    wg.player_two = [(3, 'Heart'), (4, 'Heart'), (5, 'Heart'), (6, 'Heart'), (7, 'Heart')]
    assert wg.win_check() == None
    
    wg.player_one = []
    wg.player_two = [(3, 'Heart'), (4, 'Heart'), (5, 'Heart'), (6, 'Heart'), (7, 'Heart')]
    assert wg.win_check() == True
    
    wg.player_one = [(3, 'Heart'), (4, 'Heart'), (5, 'Heart'), (6, 'Heart'), (7, 'Heart')]
    wg.player_two = []
    assert wg.win_check() == True
    
def test_game_over():
    wg.player_one = []
    wg.player_two = [(3, 'Heart'), (4, 'Heart'), (5, 'Heart'), (6, 'Heart'), (7, 'Heart')]
    assert wg.game_over() == False
    
    wg.player_one = [(3, 'Heart'), (4, 'Heart'), (5, 'Heart'), (6, 'Heart'), (7, 'Heart')]
    wg.player_two = []
    assert wg.game_over() == False
    
def test_all_cards_equal():
    wg.round_cards = [(3, 'Heart'), (3, 'Diamond'), (3, 'Club'), (3, 'Spade')]
    assert wg.all_cards_equal() == True
    
    wg.round_cards = [(3, 'Heart'), (4, 'Diamond'), (5, 'Club'), (6, 'Spade')]
    assert wg.all_cards_equal() == False