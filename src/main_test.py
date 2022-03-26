from random import shuffle
from main import *

def test_play_round():
    assert warGame.play_round(2) == 1
    
def test_compare_cards():
    assert warGame.compare_cards(3, 2) == 1
    assert warGame.compare_cards(2, 2) == 0
    assert warGame.compare_cards(2, 3) == -1 
    
def test_initialise_deck():
    assert len(warGame.initialise_deck()) == 52
    
def test_shuffle_deck():
    deck = warGame.initialise_deck()
    assert warGame.shuffle_deck(deck) != deck

def test_initialise_players():
    assert len(warGame.initialise_players(2)) == 2

def test_get_card():
    deck = warGame.initialise_deck()
    player = []
    player.append(warGame.get_card(warGame.shuffle_deck(deck), 0))
    assert len(player) == 1

def test_deal():
    deck = warGame.initialise_deck()
    num_players = 4
    players = warGame.initialise_players(num_players)
    players = warGame.deal(warGame.shuffle_deck(deck), players)
    assert len(players[0]) == 52 / num_players
    
