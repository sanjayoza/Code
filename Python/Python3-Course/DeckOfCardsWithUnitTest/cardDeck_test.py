import unittest
from CardDeck import Card
from CardDeck import Deck

class CardTests(unittest.TestCase):
    def setUp(self):
        self.card = Card("A", "Hearts")
    def test_init(self):
        """Card should have a suit and value"""
        self.assertEqual(self.card.suit, "Hearts")
        self.assertEqual(self.card.value, "A")
    def test_repr(self):
        """repr should return string 'VALUE of SUITE'"""
        self.assertEqual(repr(self.card), "A of Hearts")

class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
    def test_init(self):
         """Deck should have cards as list of length 52 """
         self.assertTrue(isinstance(self.deck.cards, list))
         self.assertEqual(len(self.deck.cards), 52)
    def test_repr(self):
        """should be 'Deck of 52 cards'"""
        self.assertEqual(repr(self.deck), "Deck of 52 cards")
    def test_count(self):
        """ count should return 52 here"""
        self.assertEqual(self.deck.count(), 52)
        self.deck.cards.pop()
        self.assertEqual(self.deck.count(), 51)
    def test_deal_sufficient_cards(self):
        """_deal should deal sufficient number of cards"""
        cards = self.deck._deal(10)
        self.assertEqual(len(cards), 10)
        self.assertEqual(self.deck.count(), 42)
    def test_deal_insufficient_cards(self):
        """should only deal 52 cards"""
        cards = self.deck._deal(100)
        self.assertEqual(len(cards), 52)
        self.assertEqual(self.deck.count(), 0)
    def test_deal_no_cards(self):
        """_deal should throw ValueError is deck is empty"""
        self.deck._deal(self.deck.count())
        with self.assertRaises(ValueError): self.deck._deal(1)
        
    def test_deal_card(self):
        """deal_card should only deal 1 card"""
        card = self.deck.cards[-1]
        dealt_card = self.deck.deal_card()
        self.assertEqual(card , dealt_card)
        self.assertEqual(self.deck.count(), 51)
    def test_deal_hand(self):
        """test deal_hand and should return number of cards requested"""
        cards = self.deck.deal_hand(20)
        self.assertEqual(len(cards), 20)
        self.assertEqual(self.deck.count(), 32)
    def test_shuffle_full_deck(self):
        """ shuffle deck should shuffle full deck"""
        cards = self.deck.cards[:]
        self.deck.shuffle()
        self.assertNotEqual(cards, self.deck.cards)
        self.assertEqual(self.deck.count(), 52)
    def test_shuffle_not_full_deck(self):
        """remove couple of cards and then shuffle should throw ValueError"""
        self.deck.deal_card()
        with self.assertRaises(ValueError): self.deck.shuffle()
        
                
if __name__ == "__main__":
    unittest.main()