# main.py
from card_deck import DeckOfCards

# Create a deck of cards
deck = DeckOfCards()
deck.shuffle()

# Deal cards to players
player1_hand, player2_hand = deck.deal()

# Show player hands
print("Player 1's Hand:")
player1_hand.show_hand()

print("\nPlayer 2's Hand:")
player2_hand.show_hand()
    