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
        "Ace": 14,
    }

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.rank_value = self.rank_values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = self.create_deck()

    def create_deck(self):
        suits = ["♦️", "♠️", "♥️", "♣️"]
        ranks = list(Card.rank_values.keys())
        return [Card(rank, suit) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        mid = len(self.cards) // 2
        return self.cards[:mid], self.cards[mid:]


class Player:
    def __init__(self, name, hand=None):
        self.name = name
        self.hand = hand if hand else []

    def play(self):
        return self.hand.pop(0) if self.has_cards() else None

    def add_card(self, card):
        self.hand.append(card)

    def has_cards(self):
        return len(self.hand) > 0


class Game:
    def __init__(self, player1, player2):
        self.deck = Deck()
        self.deck.shuffle()
        player1_hand, player2_hand = self.deck.deal()
        self.player1 = Player(player1, player1_hand)
        self.player2 = Player(player2, player2_hand)
        self.round_number = 0

    def play_round(self):
        if not self.player1.has_cards():
            print(f"{self.player2.name} wins! {self.player1.name} has no cards left.")
            return False
        if not self.player2.has_cards():
            print(f"{self.player1.name} wins! {self.player2.name} has no cards left.")
            return False

        card1 = self.player1.play()
        card2 = self.player2.play()

        print(f"{self.player1.name} plays {card1}")
        print(f"{self.player2.name} plays {card2}")

        if card1.rank_value > card2.rank_value:
            self.player1.hand.extend([card1, card2])
            print(f"{self.player1.name} wins the round")
        elif card1.rank_value < card2.rank_value:
            self.player2.hand.extend([card1, card2])
            print(f"{self.player2.name} wins the round")
        else:
            print("War!")
            self.war(card1, card2)
        return True

    def war(self, card1, card2):
        war_cards = [card1, card2]
        while True:
            if len(self.player1.hand) < 4:
                print(
                    f"{self.player1.name} does not have enough cards for a War. {self.player2.name} wins the game!"
                )
                self.player2.hand.extend(war_cards + self.player1.hand)
                self.player1.hand.clear()
                self.game_over = True
                return
            if len(self.player2.hand) < 4:
                print(
                    f"{self.player2.name} does not have enough cards for a War. {self.player1.name} wins the game!"
                )
                self.player1.hand.extend(war_cards + self.player2.hand)
                self.player2.hand.clear()
                self.game_over = True
                return

            war_cards.extend([self.player1.play() for _ in range(3)])
            war_cards.extend([self.player2.play() for _ in range(3)])
            card1 = self.player1.play()
            card2 = self.player2.play()
            war_cards.extend([card1, card2])

            print(f"{self.player1.name} plays {card1}")
            print(f"{self.player2.name} plays {card2}")

            if card1.rank_value > card2.rank_value:
                self.player1.hand.extend(war_cards)
                print(f"{self.player1.name} wins the war")
                break
            elif card1.rank_value < card2.rank_value:
                self.player2.hand.extend(war_cards)
                print(f"{self.player2.name} wins the war")
                break
            else:
                print("Another war!")
                self.war(card1, card2)

    def find_winner(self):
        if len(self.player1.hand) > len(self.player2.hand):
            return f"{self.player1.name} wins the game!"
        elif len(self.player1.hand) < len(self.player2.hand):
            return f"{self.player2.name} wins the game!"

    def play_game(self):
        while self.player1.has_cards() and self.player2.has_cards():
            print(f"Round {self.round_number + 1}:")
            self.play_round()
            self.round_number += 1
        print(self.find_winner())


if __name__ == "__main__":
    game = Game("Billy", "Johnny")
    game.play_game()
