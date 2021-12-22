import random
import itertools
from card import Card

class Deck:
    suits = ["♥", "♦", "♠", "♣"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self):
        self.cards = []

    def __len__(self):
        return len(self.cards)

    def fill_deck(self):
        """Load deck with 6 decks of cards"""
        for i in range(0, 6):
            for suit, value in itertools.product(self.suits, self.values):
                self.cards.append(Card(suit, value))

    def clear_deck(self):
        self.cards = []

    def shuffle(self):
        random.shuffle(self.cards)
