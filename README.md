# War (Card Game) | Python

Scenario by: Patrick R

![Cards Painting](./src/img/cards.jpg)

## Description

This kata is a version of the classic card game [War](http://en.wikipedia.org/wiki/War_%28card_game%29).
Credit to [gigasquid's/wonderland-clojure-katas](https://github.com/gigasquid/wonderland-clojure-katas/tree/master/card-game-war) repository as hosted on GitHub. This kata was implemented for a **coding dojo** hosted for Deloitte Core Business Operations (CBO).

The rules of this card game are quite simple.

### Base Game

- There are two players.
- The cards are all dealt equally to each player.
- Each round, player 1 lays a card down face up at the same time that
  player 2 lays a card down face up. Whoever has the highest value
  card, wins both round and takes both cards.
- The winning cards are added to the bottom of the winners deck.
- Aces are high.
- If both cards are of equal value - three cards are dealt from each hand face down and then 1 more face up to war again. the winner takes all the cards. If this ties repeat the process again.
- The player that runs out of cards loses.

### Extended Game

- Extend the game to N players
- If you capture a King, the all players must give you 4 extra cards.
- If you capture a Queen, you must give the all opponents 4 extra cards.
- If a King takes a Queen of the same suit, that player wins.

> Note: `Capture` is defined as winning a card via normal play, i.e. an Ace card takes the King card, or won as part of the face down pile during a tie resolution. Kings or Queens that are won as part of the four (4) extra cards given or recieved do not trigger the same rules again.

## Dojo Rules

- Use test driven development (TDD)
- Tests must pass

## Usage

### Setup

```zsh
pipenv install
pipenv shell
pip3 install pytest pytest-watch
```

Please note that the above is already performed if you are using the DevContainer.

### Testing

```zsh
pytest -vv
# or to run continuously
ptw -- -vv
```

## Acknowledgements

This project was developed and completed by Jim Kelly.
