from random import choice

class BiddingStrategy:
    def __init__(self):
        pass

    def choose_card(self, player_cards, diamond_card, opponent_cards):
        # Implement bidding strategy
        pass

class RandomStrategy(BiddingStrategy):
    def __init__(self):
        super().__init__()

    def choose_card(self, player_cards, diamond_card, opponent_cards):
        # Implement random bidding strategy
        return choice(player_cards)

class AdvancedStrategy(BiddingStrategy):
    def __init__(self):
        super().__init__()

    def choose_card(self, player_cards, diamond_card, opponent_cards):
        # Implement advanced bidding strategy
        available_cards = [card for card in player_cards if card.value > diamond_card.value]
        if available_cards:
            return min(available_cards, key=lambda x: x.value)
        else:
            return min(player_cards, key=lambda x: x.value)