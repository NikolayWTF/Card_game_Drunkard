from Deck import Deck
from Player import Player


class Game:
    def __init__(self):
        name1 = input("Имя игрока 1: ")
        name2 = input("Имя игрока 2: ")
        self.deck = Deck()
        self.player1 = Player(name1)
        self.player2 = Player(name2)

    @staticmethod
    def wins(winner):
        print(f"{winner} забирает карты\n")

    @staticmethod
    def draw(p1n, p1c, p2n, p2c):
        print(f"{p1n} кладёт {p1c}, а {p2n} кладёт {p2c}")

    @staticmethod
    def winner(p1, p2):
        if p1.wins > p2.wins:
            return p1.name + " выиграл!"
        if p1.wins < p2.wins:
            return p2.name + " выиграл!"
        return "Ничья!"

    def play_game(self):
        cards = self.deck.cards
        print("Игра началась")
        while len(cards) >= 2:
            response = input("Нажмите Q для выхода. Нажмите любую другую клавишу для начала игры")
            if response == "Q":
                break
            player1_card = self.deck.rm_card()
            player2_card = self.deck.rm_card()
            player1_name = self.player1.name
            player2_name = self.player2.name
            self.draw(player1_name, player1_card, player2_name, player2_card)
            if player1_card > player2_card:
                self.player1.wins += 1
                self.wins(self.player1.name)
            else:
                self.player2.wins += 1
                self.wins(self.player2.name)

        win = self.winner(self.player1, self.player2)

        print(f"Игра окончена. {win}")
