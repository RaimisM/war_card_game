import random

def main():
    ...

def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    return deck

def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

def player_one():
    ...

def winning_move():
    ...

if __name__ == "__main__":
    main()

# Example usage
deck = create_deck()
shuffled_deck = shuffle_deck(deck)
print(shuffled_deck)
