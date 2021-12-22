import time
from deck import Deck
from human import Human
from dealer import Dealer

class Game:
    players = []
    deck = []
    playerbet = 0
    players_turn = True

    def deal(self):
        '''
        Appending any 4 cards
        '''

        if len(self.deck) < 104:  
            self.deck.clear_deck()
            self.deck.fill_deck()
            self.deck.shuffle()
            time.sleep(4)
        for i in range(2):
            for player in self.players:
                card = self.deck.cards.pop()
                player.hand.append(card)

    def hit(self, player):
        card = self.deck.cards.pop()
        player.hand.append(card)
        if isinstance(player, Dealer):
            player.show_hand(True)
        else:
            player.show_hand()
        self.checkbust(player)
        print(f"player point is {player.point_ace_adjusted}")

    def playerchoice(self, player):
        answer = input("Hit or Stick? h/s: ")
        if answer.lower() == "h":
            self.hit(player)
        if answer.lower() == "s":
            print(f"Player Sticks with hand of {str(player.point_ace_adjusted)}\n")
            self.players_turn = False

    def checkbust(self, player):
        if player.isbusted:
            if isinstance(player, Human):
                print("Player Busts!")
                self.players_turn = False
                self.playerlose()
            if isinstance(player, Dealer):
                print("\nDealer Busts!")

    def playerwin(self, player):
        print(f"You win! \n{str(2 * self.playerbet)} chips added to your total.")
        player.chips += 2 * self.playerbet
        self.playerbet = 0

    def playerlose(self):
        print(f"You lose!")

    def draw(self, player):
        print(f"Its a draw, you get your bet of {self.playerbet} back.")
        player.chips += self.playerbet

    def comparescores(self, player, dealer):
        if player.point_ace_adjusted > dealer.point_ace_adjusted:
            self.playerwin(player)
        if player.point_ace_adjusted == dealer.point_ace_adjusted:
            self.draw(player)
        if player.point_ace_adjusted < dealer.point_ace_adjusted:
            self.playerlose()

    def resetplayers(self):
        for player in self.players:
            player.reset()
        self.playerbet = 0

    def playagain(self, player):
        again = None
        while again != "y" or again != "n":
            again = input("\nWould you like to play again? Y/N: ")
            if again.lower() == "y":
                return True
            if again.lower() == "n":
                print(f"\nOk, thanks for playing. You walk away with {player.chips} chips.")
                return False
            else:
                print("That was not a valid input")

    def play(self):
        print("---------- Welcome to Blackjack ----------")
        self.deck = Deck()
        player = Human(100)
        dealer = Dealer()
        self.players = [player, dealer]
        self.deck.fill_deck()
        self.deck.shuffle()
        running = True
        
        while running:
            if self.players[0].chips == 0:
                print("You are flat broke! It's time to leave the table.")
                input("Press any key to walk away in shame.")
                break
            self.playerbet = player.place_bet()
            self.deal()
            dealer.show_hand()
            player.show_hand()
            while self.players_turn:
                self.playerchoice(player)
            if not player.isbusted:
                dealer.show_hand(True)
                while not self.players_turn:
                    if dealer.point_ace_adjusted < 17:
                        time.sleep(1)
                        print("\nDealer Hits")
                        self.hit(dealer)
                        time.sleep(1)
                    if dealer.point_ace_adjusted >= 17 and not dealer.isbusted:
                        print(f"\nDealer Sticks with hand of {str(dealer.point_ace_adjusted)}\n")
                        break
                    if dealer.isbusted:
                        self.playerwin(player)
                        break
                if not dealer.isbusted:
                    self.comparescores(player, dealer)
            again = self.playagain(player)
            if not again:
                running = False
            self.players_turn = True
            self.resetplayers()