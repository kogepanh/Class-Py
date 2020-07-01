# ex05

class Card:
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        if self.rank == 1:
            self.rank = 14
    
    def __str__(self):
        return f"カードは {self.suits[self.suit-1]}{self.ranks[self.rank-1]} です"

    def compare(self, card2):
        if card1.suit > card2.suit:
            winner = card1
        elif card1.suit < card2.suit:
            winner = card2
        else:
            if card1.rank > card2.rank:
                winner = card1
            elif card1.rank < card2.rank:
                winner = card2
            else:
                return f"引き分けです"
        return f"{self.suits[winner.suit-1]}{self.ranks[winner.rank-1]} の勝ち"

# main
import random
for i in range(10):
    card1 = Card(random.randrange(1, 4), random.randrange(1, 13))
    card2 = Card(random.randrange(1, 4), random.randrange(1, 13))
    print(card1)
    print(card2)
    print(card1.compare(card2))
