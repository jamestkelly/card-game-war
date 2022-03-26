# card-game-war

Scenario by: Patrick R

![Cards Painting](/images/cardspainting.gif)

This kata is a version of the classic card game [War](http://en.wikipedia.org/wiki/War_%28card_game%29).
Credit to [gigasquid's /wonderland-clojure-katas repo](https://github.com/gigasquid/wonderland-clojure-katas/tree/master/card-game-war).

The rules of this card game are quite simple.

- There are two players.
- The cards are all dealt equally to each player.
- Each round, player 1 lays a card down face up at the same time that
  player 2 lays a card down face up.  Whoever has the highest value
  card, wins both round and takes both cards.
- The winning cards are added to the bottom of the winners deck.
- Aces are high.
- If both cards are of equal value - three cards are dealt from each hand face down and then 1 more face up to war again. the winner takes all the cards. If this ties repeat the process again.
- The player that runs out of cards loses.
  
___
If finished early, implement these additional rules

- Extend the game to N players
- If you capture a King, the all players must give you 4 extra cards.
- If you capture a Queen, you must give the all opponents 4 extra cards.
- If a King takes a Queen of the same suit, that player wins.

> Capture is defined as winning a card via normal play (ie Ace takes King) or won as part of the face down pile during a tie resolution. Kings or Queens won as part of the 4 extra cards given or recieved do not trigger the same rules again.

## Dojo

- Use TDD
- Make tests pass!

## Usage

Setup:

```zsh
pipenv install
pipenv shell
pip3 install pytest pytest-watch
```

Please note that the above is already performed if you are using the DevContainer.

Run tests:

```zsh
pytest -vv
# or to run continuously 
ptw -- -vv
```
