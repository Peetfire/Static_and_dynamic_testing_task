#from _typeshed import Self
import unittest
from unittest import result

from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("hearts", 1)
        self.card2 = Card("clubs", 5)
        self.card3 = Card("diamonds", 11)
        self.card4 = Card("spades", 9)
        self.hand = [self.card1, self.card2, self.card3, self.card4]
        self.game = CardGame()

    def test_check_for_ace(self):
        expected = True
        result = self.game.check_for_ace(self.card1)
        self.assertEqual(expected, result)

    # @unittest.skip("not witten yet")     
    def test_highest_card(self):
        expected = self.card3
        result = self.game.highest_card(self.card3, self.card4)
        self.assertEqual(expected, result)

    # @unittest.skip("not witten yet")   
    def test_cards_total(self):
        expected = "You have a total of 26"
        result = self.game.cards_total(self.hand)
        self.assertEqual(expected, result)