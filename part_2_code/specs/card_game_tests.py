from _typeshed import Self
import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame:

    def setUp(self):
        self.card1 = Card("hearts", 1)
        self.card2 = Card("clubs", 5)
        self.card3 = Card("diamonds", 11)
        self.card4 = Card("spades", 9)
        self.hand = [self.card1, self.card2, self.card3, self.card4]

    def test_check_for_ace(self):
        pass

    def test_highest_card(self):
        pass

    def test_cards_total(self):
        pass