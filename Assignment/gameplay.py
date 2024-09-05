from random import shuffle, choice
from strategies import BiddingStrategy

class Card:
    def __init__(self, value):
        self.value = value

class Player:
    def __init__(self):
        self.cards = []
        self.score = 0

    def calculate_score(self, diamond_card_value):
        self.score += diamond_card_value

class Game:
    def __init__(self, player_strategy):
        self.diamond_cards = [Card(value) for value in range(2, 14)]
        self.player = Player()
        self.opponent = Player()
        self.diamond_card = None
        self.prime_cards = [10, 11, 12, 13]
        self.player_strategy = player_strategy

    def play_round(self):
        shuffle(self.diamond_cards)
        self.diamond_card = choice(self.diamond_cards)
        print(f"Diamond Card: {self.diamond_card.value}")

        # Player's move
        user_input = int(input("Enter your card value (2-13): "))
        while user_input not in range(2, 14) or user_input not in [card.value for card in self.opponent.cards]:
            print("Invalid input. Please enter a valid card value.")
            user_input = int(input("Enter your card value (2-13): "))

        opponent_card = next(card for card in self.opponent.cards if card.value == user_input)
        self.opponent.cards.remove(opponent_card)

        # Computer's move
        computer_card = self.player_strategy.choose_card(self.player.cards, self.diamond_card, self.opponent.cards)
        self.player.cards.remove(computer_card)

        # Determine winner and update scores
        if computer_card.value > opponent_card.value:
            self.player.calculate_score(self.diamond_card.value)
        elif computer_card.value < opponent_card.value:
            self.opponent.calculate_score(self.diamond_card.value)
        else:
            self.player.calculate_score(self.diamond_card.value / 2)
            self.opponent.calculate_score(self.diamond_card.value / 2)

        # Display scores after each round
        print(f"Player's Score: {self.player.score}")
        print(f"Opponent's Score: {self.opponent.score}")

        # Remove the chosen diamond card from the deck
        self.diamond_cards.remove(self.diamond_card)

    def start_game(self):
        self.player.cards = [Card(value) for value in range(2, 14)]
        self.opponent.cards = [Card(value) for value in range(2, 14)]
        while len(self.diamond_cards) > 0:
            self.play_round()
        print("Game Over!")
        print(f"Player's Score: {self.player.score}")
        print(f"Opponent's Score: {self.opponent.score}")
        if self.player.score > self.opponent.score:
            print("Player Wins!")
        elif self.player.score < self.opponent.score:
            print("Opponent Wins!")
        else:
            print("It's a Tie!")

# Example usage:
from strategies import AdvancedStrategy
game = Game(AdvancedStrategy())
game.start_game()