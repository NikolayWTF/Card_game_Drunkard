class Card:
    suits = ["крести", "буби", "черва", "пики"]

    values = [None, None, "2", "3", "4", "5",
              "6", "7", "8", "9", "10", "валет",
              "дама", "король", "туз"]

    def __init__(self, v: int, s: int):
        self.value = v
        self.suit = s

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
        return False

    def __repr__(self):
        card_name = self.values[self.value] + " " + self.suits[self.suit]
        return card_name
