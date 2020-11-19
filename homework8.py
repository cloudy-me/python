from random import randrange
import itertools
import sys


class Card:

    @staticmethod
    def card():
        i = 0
        _card = []
        while i < 3:
            line = []
            while len(line) < 5:
                el = randrange(1, 91)
                line.append(el)
            line.sort()
            _line_final = []
            j = 0
            k = 0  # number of empty cells (0-3)
            while j < 5 and k < 4:
                prob = randrange(3)
                if prob < 2:
                    _line_final.append(line[j])
                    j += 1
                else:
                    _line_final.append("-")
                    k += 1

            while len(_line_final) < 9:
                if k < 4:
                    _line_final.append("-")
                    k += 1
                else:
                    _line_final.append(line[j])
                    j += 1

            i += 1
            _card.append(_line_final)
        return _card


class Start(Card):

    def __init__(self):
        self.player = self.card()
        self.computer = self.card()

    @property
    def start(self):
        print('Game start')
        print('--------Your card------')
        print(self._print_player(self.player))
        print('-----Computer card-----')
        print(self._print_player(self.computer))

    def _print_player(self, item):
        item = ('\n'.join([' '.join([str(elem) for elem in line]) for line in item]) + '\n' + '-' * 23)
        return item


class Play(Start):

    def __init__(self):
        super().__init__()
        self.answer = 'y'
        self.num = 0
        self.player_x = 0  # счетчик для игрока (0-15)
        self.computer_x = 0  # счетчик для компьютера (0-15)

    @property
    def play(self):

        while self.player_x < 15 or self.computer_x <15:
            self.num = randrange(1, 91)
            print('New number', self.num)
            self.answer = input('Cross the number (y/n)?')
            self.player_choice()
            self.computer_round()
            self.print_updated_cards()
        else:
            sys.exit('Game over')

    def player_choice(self):

        cross_term = 0
        for line in self.player:
            cross_term += line.count(self.num)

        if self.answer == 'n' and cross_term == 0:
            pass
        elif self.answer == 'y' and cross_term > 0:
            for line in self.player:
                for el, item in enumerate(line):
                    if item == self.num:
                        item = 'x'
                        line[el] = item
            self.player_x += cross_term
        else:
            sys.exit('Game over')

    def computer_round(self):

        cross_term = 0
        for line in self.computer:
            cross_term += line.count(self.num)

        if cross_term > 0:
            for line in self.computer:
                for el, item in enumerate(line):
                    if item == self.num:
                        item = 'x'
                        line[el] = item
            self.computer_x += cross_term

    def print_updated_cards(self):
        print('--------Your card------')
        print(self._print_player(self.player))
        print('-----Computer card-----')
        print(self._print_player(self.computer))

class Game(Play):
    pass

game = Game()
game.start
game.play

