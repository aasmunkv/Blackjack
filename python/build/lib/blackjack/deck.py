from collections import deque

from blackjack.suit import Suit
from blackjack.card import Card

class Deck:
    def __init__(self):
        """
        This initializes a deck of cards with all 52 cards.
        """
        self.cards = deque()

        for suit in Suit:
            for i in range(1, 14):
                rank = "A"*(i==1) + "J"*(i==11) + "Q"*(i==12) + "K"*(i==13)
                self.cards.append(Card(rank=rank, suit=suit))