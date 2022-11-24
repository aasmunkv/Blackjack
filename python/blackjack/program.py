"""
This file consist of the outer structure of my little casino experience.
Each game of blackjack runs using the implemented 'Game' object.
"""

from blackjack.game import Game

separator = "-----------------------------------------"

def main():
    while True:
        try:
            wallet = int(input(f"{separator}\nWallet amount: "))
            break
        except:
            print("Please insert a valid integer.")
    print(separator)
    print("Welcome to the casino.\nLet's play some blackjack!")
    while True:
        if wallet <= 0:
            print(
                f"{separator}\nI am sorry to inform that you are broke.\n" +
                "You are welcome to play another time.\n" +
                "With money of course!"
            )
            break
        print(f"{separator}\nYour current balance is:", wallet)
        read = input(f"{separator}\nTake your winnings (t) or play (p): ")
        if read == "t":
            print(f"{separator}\nHave a nice evening!\nBut don't spend it all in one place!")
            break
        elif read == "p":
            game = Game()
            while True:
                try:
                    bet = int(input(f"{separator}\nAmount to bet: "))
                    if bet > wallet:
                        print("You cannot bet more money than you have!")
                    else:
                        break 
                except:
                    print("Please insert a valid integer.")
            payoff = game.play()
            wallet += payoff*bet
        else:
            print("Please type a valid option: [t/p]")

if __name__ == "__main__":
    main()
