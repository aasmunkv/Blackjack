'''
author: Åsmund Danielsen Kvitvang

This file contains the main content for the Blackjack simulator.
main()-function runs the outer structure of the game such as the players wallet and winnings.
play()-function contains the actual balckjack game, which consist of one round against the dealer.
getHandTotal(), dealersPlay() and printWinner() are help functions used at multiple occations.
'''

from blackjack.deck import Deck
import numpy as np

'''
TODO:
- Sørg for å være konsistent på navning. Bruk enten notasjon a_b eller aB, men ikke begge.
- Pass på at ingenting unødvendig er hardkodet.
- Flytt ting som bør flyttes til andre fil-lokasjoner.
- Vær konsistent på bruken av fnutter. Velg enten " eller '.
- Skriv et konsist sammendrag av hvilke forandringer som er blitt gjort.
'''

separator = "-----------------------------------------"
#suitSymbols = {"Spades": "♠", "Hearts": "♥", "Clubs": "♣", "Diamonds": "♦"}
#suitSymbols = {"Spades": "\u2660", "Hearts": "\u2665", "Clubs": "\u2663", "Diamonds": "\u2666"}

def main():
    while True:
        try:
            wallet = int(input("Wallet amount: "))
            break
        except:
            print("Please insert a valid integer.")
    print(separator)
    print("Welcome to the casino.\nLet's play some blackjack!")
    while True:
        if wallet <= 0:
            print(separator +
                "\nI am sorry to inform that you are broke.\n"+
                "You are welcome to play another time.\n"+
                "With money of course!"
            )
            break
        print(separator+"\nYour current balance is:", wallet)
        read = input(separator+"\nTake your winnings (t) or play (p): ")
        if read == 't':
            print(separator+"\nHave a nice evening!\nBut don't spend it all in one place!")
            break
        elif read == 'p':
            while True:
                try:
                    bet = int(input("Amount to bet: "))
                    if bet > wallet:
                        print("You cannot bet more money than you have!")
                    else:
                        break 
                except:
                    print("Please insert a valid integer.")
            payoff = play()
            wallet += payoff*bet
        else:
            print("Please type a valid option: [t/p]")

    

def play():
    deck = Deck()
    hand = []
    dealer = []
    payoff = 1
    # start dealing to player and dealer
    print("Starting to deal cards...")
    print(separator)
    for i in range(2):
        card_hand = deck.cards.pop()
        card_dealer = deck.cards.pop()
        hand.append(card_hand)
        dealer.append(card_dealer)
        print(
            f'Hand: {card_hand.suit.name:>8s} {card_hand.rank:5s}',
            f'Dealer: {card_dealer.suit.name} {card_dealer.rank}.' if i==0 else 'Dealer: Unknown.'
        )
    print(f'Total is {getHandTotal(hand)}.')
    while True:
        print(separator)
        total = getHandTotal(hand)
        if total == 21:
            print("Winner, winner, chicken dinner!\n" + separator)
            total_dealer = dealersPlay(dealer, deck, total)
            winner = printWinner(total, total_dealer)
            payoff *= winner*1.5 # Payout is 3:2 if blackjack
            break
        else:
            read = input('Stand (s) or hit (h): ')
            if read in ['Hit', 'hit', 'H', 'h']:
                card = deck.cards.pop()
                hand.append(card)
                total = getHandTotal(hand)
                print(f'Hit with {card.suit.name} {card.rank}. Total is {total}')
                if total > 21:
                    print(separator + "\nOh snap, you hit too hard\n"+separator)
                    total_dealer = dealersPlay(dealer, deck, total)
                    winner = printWinner(total, total_dealer)
                    payoff *= winner
                    break
                elif total == 21:
                    print(separator + "\nWinner, winner, chicken dinner!\n" + separator)
                    total_dealer = dealersPlay(dealer, deck, total)
                    winner = printWinner(total, total_dealer)
                    payoff *= winner
                    break
            elif read in ['Stand', 'stand', 'S', 's']:
                print("Standing down. Dealers turn.")
                print(separator)
                total_dealer = dealersPlay(dealer, deck, total)
                winner = printWinner(total, total_dealer)
                payoff *= winner
                break
    return payoff

def getHandTotal(hand):
    total = sum([
        10 if card.rank in ["J", "Q", "K"] 
        else ( 0 if card.rank=="A" else int(card.rank) ) 
        for card in hand
    ])
    # Going through all aces on hand and adding highest possible score without exceeding 21.
    ace_cnt = sum([card.rank=="A" for card in hand])
    if ace_cnt > 0:
        ace_combinations = np.array([
            [1, 11],            # 1 ace at hand
            [2, 12, 22],        # 2 aces at hand
            [3, 13, 23, 33],    # 3 aces at hand
            [4, 14, 24, 34, 44] # 4 aces at hand
        ][ace_cnt-1])
        total += max(
            ace_combinations[(total + ace_combinations) <= 21], 
            default = min(ace_combinations)
        )
    return total

def dealersPlay(hand, deck, stoppingPoint):
    '''
    Dealers game is to draw cards until the score exceeds the players score.
    '''
    total = getHandTotal(hand)
    print(
        f'Dealers initial total is {total} with cards\n' +
        ' and '.join([f'{card_dealer.suit.name} {card_dealer.rank}' for card_dealer in hand])
    )
    while ((total <= stoppingPoint) and (stoppingPoint <= 21)) and (total != 21):
        card_dealer = deck.cards.pop()
        hand.append(card_dealer)
        total = getHandTotal(hand)
        print(separator)
        print(f'Dealer drew: {card_dealer.suit.name:>8s} {card_dealer.rank:5s} Total is {total}.')
    return total

def printWinner(total, total_dealer):
    '''
    Print who's the winner based on dealer and player totals.
    '''
    print(separator)
    if ((total_dealer < total) or (total_dealer > 21)) and (total <= 21):
        print("You win!")
        return 1
    elif ((total < total_dealer) or (total > 21)) and (total_dealer <= 21):
        print("Dealer wins.")
        return -1
    else:
        print("It's a draw.")
        return 0

if __name__ == '__main__':
    main()
