class Player:
    def __init__(self):
        self.hand = []

    def show_hand(self):
        print("\nPlayers Hand:")
        for n, card in enumerate(self.hand):
            print(str(self.hand[n]))
        print()

    def reset(self):
        self.hand = []

    @property
    def ace_count(self):
        return len([c for c in self.hand if c.value == "Ace"])

    @property
    def point(self):
        return sum([c.cardscore for c in self.hand])

    @property
    def point_ace_adjusted(self):
        for ace in range(self.ace_count):
            if self.point < 12:
                self.point += 10
        return self.point

    @property
    def isbusted(self):
        if self.point_ace_adjusted > 21:
            return True

