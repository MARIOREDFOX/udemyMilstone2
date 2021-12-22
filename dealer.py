from player import Player

class Dealer(Player):
    def __init__(self):
        super().__init__()
        self.hand = []

    def show_hand(self, showall=False):
        """Prints out the dealers hand,to show all cards or only shows first card"""
        print("\nDealer's Hand:")
        if showall:
            for n, card in enumerate(self.hand):
                print(str(self.hand[n]))
                print(str(card))
        else:
            print(str(self.hand[0]))
            print("--???--")
