from blackjack.deck import Deck
import numpy as np

class Game:
    """
    This object contains all necessary methods for a nice game of old fashion blackjack.

    play() consists of the outer structure of the game where the player have some stand/hit options.
    getHandTotal(hand) calculated the total number of points based on the hand of cards sent in as
        a parameter.
    dealersPlay() consists of the dealers actions during a round of blackjack. The dealer draws 
        cards until reaching 17 or more points.
    endPlay() consists of the final parts of a round, namely dealersPlay and announcing winner.
    printWinner() prints out the winner based on dealers and players points.
    """
    def __init__(self):
        self.deck = Deck()
        self.handPlayer = []
        self.handDealer = []
        self.totalPlayer = 0
        self.totalDealer = 0
        self.payoff = 1.0
        self.isNatural = False
        self.separator = "-----------------------------------------"
    
    def play(self):
        """
        Consists of the outer structure of the game where the player have some stand/hit options.
        Input: None
        Output: 
            payoff - the payoff (positive/negative) to the player, type: float
        """
        print("Starting to deal cards...")
        print(self.separator)
        for i in range(2):
            cardHand = self.deck.cards.pop()
            cardDealer = self.deck.cards.pop()
            self.handPlayer.append(cardHand)
            self.handDealer.append(cardDealer)
            print(
                f"Hand: {cardHand.suit.name:>8s} {cardHand.rank:5s}",
                f"Dealer: {cardDealer.suit.name} {cardDealer.rank}." if i==0 else "Dealer: Unknown."
            )
        print(f"Total is {self.getHandTotal(self.handPlayer)}.")
        while True:
            self.totalPlayer = self.getHandTotal(self.handPlayer)
            if self.totalPlayer == 21:
                self.isNatural = True
                self.payoff *= 1.5 # Payout is 3:2 if natural/blackjack
                self.endPlay(f"{self.separator}\nWinner, winner, chicken dinner!")
                break
            else:
                read = input(f"{self.separator}\nStand (s) or hit (h): ")
                if read in ["Hit", "hit", "H", "h"]:
                    card = self.deck.cards.pop()
                    self.handPlayer.append(card)
                    self.totalPlayer = self.getHandTotal(self.handPlayer)
                    print(f"Hit with {card.suit.name} {card.rank}. Total is {self.totalPlayer}")
                    if self.totalPlayer > 21:
                        self.endPlay(f"{self.separator}\nOh snap, you hit too hard")
                        break
                    elif self.totalPlayer == 21:
                        self.endPlay(f"{self.separator}\nWinner, winner, chicken dinner!")
                        break
                elif read in ["Stand", "stand", "S", "s"]:
                    self.endPlay("Standing down. Dealers turn.")
                    break
        return self.payoff

    def getHandTotal(self, hand):
        """
        Calculates the total number of points based on the hand of cards sent in as a parameter.
        Input:
            hand - hand of cards, type: list
        Output
            total - total number of points in hand, type: integer
        """
        total = sum([
            10 if card.rank in ["J", "Q", "K"] 
            else ( 0 if card.rank=="A" else int(card.rank) ) 
            for card in hand
        ])
        # Going through all aces on hand and adding highest possible score without exceeding 21.
        aceCount = sum([card.rank=="A" for card in hand])
        if aceCount > 0:
            aceCombinations = np.array([
                [1, 11],            # 1 ace at hand
                [2, 12, 22],        # 2 aces at hand
                [3, 13, 23, 33],    # 3 aces at hand
                [4, 14, 24, 34, 44] # 4 aces at hand
            ][aceCount-1])
            total += max(
                aceCombinations[(total + aceCombinations) <= 21], 
                default = min(aceCombinations)
            )
        return total

    def dealersPlay(self):
        """
        Dealers game is to draw cards until the score exceeds 17 points.
        If player gets a "natural"/blackjack, the player wins unless dealer also gets a natural.
        """
        self.totalDealer = self.getHandTotal(self.handDealer)
        if not (self.isNatural and (self.totalDealer < 21)):
            print(
                f"{self.separator}\nDealers initial total is {self.totalDealer} with cards\n" +
                " and ".join([f"{cardDealer.suit.name} {cardDealer.rank}" for cardDealer in self.handDealer])
            )
            while (self.totalDealer < 17):
                cardDealer = self.deck.cards.pop()
                self.handDealer.append(cardDealer)
                self.totalDealer = self.getHandTotal(self.handDealer)
                print(f"{self.separator}\nDealer drew: {cardDealer.suit.name:>8s} {cardDealer.rank:5s} Total is {self.totalDealer}.")

    def printWinner(self):
        """
        Print who's the winner based on dealer and player totals.
        """
        print(self.separator)
        if ((self.totalDealer < self.totalPlayer) or (self.totalDealer > 21)) and (self.totalPlayer <= 21):
            print("You win!")
            self.payoff *= 1
        elif ((self.totalPlayer < self.totalDealer) or (self.totalPlayer > 21)) and (self.totalDealer <= 21):
            print("Dealer wins.")
            self.payoff *= -1
        else:
            print("It's a draw.")
            self.payoff *=  0

    def endPlay(self, message):
        """
        The last part of the blackjack game, i.e. the dealers turn and winner announcements.
        """
        print(message)
        self.dealersPlay()
        self.printWinner()