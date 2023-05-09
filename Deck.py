from random import shuffle
from Card import Card


class Deck:
    def __init__(self):
        self.cards = [Card(2, 0), Card(2, 1), Card(2, 2), Card(2, 3),
                      Card(3, 0), Card(3, 1), Card(3, 2), Card(3, 3),
                      Card(4, 0), Card(4, 1), Card(4, 2), Card(4, 3),
                      Card(5, 0), Card(5, 1), Card(5, 2), Card(5, 3),
                      Card(6, 0), Card(6, 1), Card(6, 2), Card(6, 3),
                      Card(7, 0), Card(7, 1), Card(7, 2), Card(7, 3),
                      Card(8, 0), Card(8, 1), Card(8, 2), Card(8, 3),
                      Card(9, 0), Card(9, 1), Card(9, 2), Card(9, 3),
                      Card(10, 0), Card(10, 1), Card(10, 2), Card(10, 3),
                      Card(11, 0), Card(11, 1), Card(11, 2), Card(11, 3),
                      Card(12, 0), Card(12, 1), Card(12, 2), Card(12, 3),
                      Card(13, 0), Card(13, 1), Card(13, 2), Card(13, 3),
                      Card(14, 0), Card(14, 1), Card(14, 2), Card(14, 3)]
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()
