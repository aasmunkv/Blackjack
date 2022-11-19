from blackjack.deck import Deck

def main():

    deck = Deck()
    hand = []

    while True:
        read = input('Stand, Hit:\n')
        if read == 'Hit':
            card = deck.cards.pop()
            hand.append(card)
            total = sum([min(card.rank, 10) for card in hand])
            print(f'Hit with {card.suit.name} {card.rank}. Total is {total}')
            if total > 21:
                print("Oh, you hit to hard, sum exceeded 21, you lost, house wins...")
                break
        elif read == 'Stand':
            break

if __name__ == '__main__':
    main()
