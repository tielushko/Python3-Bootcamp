from random import shuffle

class Card:
    allowed_suit = ("Hearts", "Diamonds", "Clubs", "Spades")
    allowed_value = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

    def __init__(self, suit, value):
        if suit in Card.allowed_suit and value in Card.allowed_value: 
            self.suit = suit
            self.value = value
        else:
            raise "You are trying to create a card of a wrong suite or wrong number!"
    
    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    cards = []
    allowed_suit = ("Hearts", "Diamonds", "Clubs", "Spades")
    allowed_value = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

    def __init__(self):
        for suit in Deck.allowed_suit:
            for value in Deck.allowed_value:
                Deck.cards.append(Card(suit, value))
    
    def __repr__(self):
        return f"Deck of {self.count()} cards" 

    def count(self):
        return len(self.cards)

    #TODO - CHECK UDEMY
    def _deal(self, amount):
        if amount < self.count():
            #remove the cards from the deck
            ret = []
            for x in range(amount):
                ret.append(self.cards.pop(0))
            return ret
        elif self.count() == 0:
            return ValueError("All cards have been dealt")
        elif amount >= self.count():
            ret = [card for card in Deck.cards]
            Deck.cards.clear()
            return ret
    
    def shuffle(self):
        if self.count() == 52:
            shuffle(self.cards)
        else: 
            raise ValueError("Only full decks can be shuffled")
        return self

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, amount):
        return self._deal(amount)

#MAIN TESTING
#
#Test From Colt
my_deck = Deck()
print(my_deck)
my_deck.shuffle()
card = my_deck.deal_card()
print(card)
hand = my_deck.deal_hand(5)
print(hand)
print(my_deck)