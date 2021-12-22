from player import Player

class Human(Player):
    def __init__(self, chips):
        super().__init__()
        self.chips = chips

    def place_bet(self):
        bet = input(f"\nYou have {self.chips} chips. \nHow much would you like to bet?: ")
        try:
            if int(bet) > self.chips:
                print("You don't have enough to bet that much!")
                self.place_bet()
            else:
                self.chips -= int(bet)
                return int(bet)
        except ValueError:
            print("That is not a valid bet entry.")
            self.place_bet()
