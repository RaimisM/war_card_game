import random

class Card:
    rank_values = {
        "2": 2, 
        "3": 3, 
        "4": 4, 
        "5": 5, 
        "6": 6, 
        "7": 7, 
        "8": 8, 
        "9": 9, 
        "10": 10, 
        "Jack": 11, 
        "Queen": 12, 
        "King": 13, 
        "Ace": 14
    }

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.rank_values = self.rank_values[rank]
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"
     

class Deck:
    def __init__(self):
        self.cards = self.create_deck()
     
    def create_deck(self):
        suits = ["♦️", "♠️", "♥️", "♣️"]
        ranks = list(Card.rank_values)
        return [Card(rank, suit) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        middle = len(self.cards) // 2
        return self.cards[:middle], self.cards[middle:]

class Player:
    def __init__(self, name, hand):

    def play(self):

    
class Game:
    def __init__():


    def play_round(self):
  
    def war(self):
       
    def find_winner(self):


    def play_game(self):


if __name__ == "__main__":


