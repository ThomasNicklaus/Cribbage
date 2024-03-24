# card_deck.py
import random

class Card:
    def __init__(self, suit, value, cribbage_counting_value):
        self.suit = suit
        self.value = value
        self.cribbage_counting_value = cribbage_counting_value
        self.in_use = False

class DeckOfCards:
    def __init__(self):
        self.cards = []
        self.create_deck()

    def create_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        cribbage_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 1}

        for suit in suits:
            for value in values:
                cribbage_counting_value = cribbage_values[value]
                self.cards.append(Card(suit, value, cribbage_counting_value))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if self.cards:
            return self.cards.pop()
        else:
            print('Deck is empty.')
            return None

    def reset_deck(self):
        self.cards = []
        self.create_deck()
        self.shuffle()

    def deal(self):
        player1_hand = PlayerHand()
        player2_hand = PlayerHand()

        for _ in range(6):
            player1_hand.add_card(self.draw_card())
            player2_hand.add_card(self.draw_card())

        player1_hand.sort_hand()
        player2_hand.sort_hand()

        return player1_hand, player2_hand

class PlayerHand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def sort_hand(self):
        # Custom sorting function based on specified card values order
        value_order = ['King', 'Queen', 'Jack', '10', '9', '8', '7', '6', '5', '4', '3', '2', 'Ace']
        self.cards.sort(key=lambda card: value_order.index(card.value))

    def show_hand(self):
        for card in self.cards:
            print(f'{card.value} of {card.suit}')
