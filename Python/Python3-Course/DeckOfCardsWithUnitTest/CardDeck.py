import random

class Card:
    
    def __init__(self, value, suit):
        self.suit =  suit
        self.value = value
        
    def __repr__(self):
        return (self.value + " of " + self.suit)



class Deck:
    def __init__(self):
        card_suite = ["Hearts", "Diamonds", "Clubs", "Spades"]
        card_value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(value, suit) for suit in card_suite for value in card_value]
    
    def count(self):
        return len(self.cards)
        
    def __repr__(self):
        count = self.count()
        count = str(count)
        return ("Deck of " + count + " cards")
    

# My implementation    
#     def _deal(self, num):
#         if self.count() == 0:
#             raise ValueError("All cards are dealt")
#         if self.count() < num:
#             num = self.count()
#         ret = list()
#         i = 0
#         while (i < num):
#             ret.append(self.cards.pop())
#             i += 1
#         return ret
    
    def _deal(self, num):
        count = self.count()
        actual = min([count, num])
        if count == 0:
            raise ValueError("All cards are dealt")
        
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards
       
    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full deck can be shuffled")
        random.shuffle(self.cards)
        return self
    
# My implementation    
#     def deal_card(self):
#         return self._deal(1)
    
    def deal_card(self):
        return self._deal(1)[0]
    def deal_hand(self, num):
        return (self._deal(num))
    
    
if __name__ == "__main__":
   
    d = Deck()
    d.shuffle()
    print(d)
    card = d.deal_card()
    print(card)
    hand = d.deal_hand(50)
    card2 = d.deal_card()
    print(card2)
    print(d.cards)
    card2 = d.deal_card()
    print(d.count())





