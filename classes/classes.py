# classes.py

# imports the random functions
import random

# Below variables are used to create Deck and assign values to each card
cards = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
cards_dict = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 0}

# Creates deck for players and dealer to play with
class Deck():
    def __init__(self):
        self.deck = [];
        for i in range(0,5):
            for card in cards:
                self.deck.append(card)
    
    def __str__(self):
        strRet = ''
        strRet = self.deck[0]
        for i in range(1, len(self.deck)):
            strRet = strRet+ " " + self.deck[i]
        return strRet
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal_card(self):
        retVal = ''
        retVal = self.deck.pop()
        return retVal
    
    def append(self, other):
        self.deck = self.deck + other.deck

# Creates hands for players
class Hand():  
    def __init__(self):
        self.current_hand = []
        self.value = 0;
        
    def print_card(self, end_Val):
        strRet = ''
        strRet = self.current_hand[0]
        for i in range(1, end_Val):
            strRet = strRet + " " + self.current_hand[i]
        return strRet
    
    def add_card(self, card):
        self.current_hand.append(card)
        value_card = cards_dict[card]
        self.value = self.value + value_card
    
    def aces_choice(self):
        while True:
            ask = input("Do you want aces to count as 1 or 11? ")
            if ask == "1":
                self.value = self.value + 1
                print("Your ace counts as a 1!")
                break
            elif ask == "11":
                self.value = self.value + 11
                print("Your ace counts as a 11!")
                break
            else:
                continue

# Creates chips for players to keep count of money
class Chips():
    def __init__(self):
        self.value = 100
        self.bet = 0
        self.insurance = 0
    
    def won_bet(self):
        self.value = self.value + self.bet
    
    def lost_bet(self):
        self.value = self.value - self.bet
        
    def won_bet_blackjack(self):
        self.value = self.value + (self.bet * 1.5)
    
    def lost_surrender(self):
        self.value = self.value - (self.bet/2)
    
    def lost_split(self):
        self.value = self.value - self.bet
        
    def won_split(self):
        self.value = self.value + self.bet
        
    def bust_split(self):
        self.value = self.value - self.bet
    
    def insurance_money_won(self):
        self.value = self.value + (self.insurance * 2)
        
    def insurance_money_loss(self):
        self.value = self.value - self.insurance