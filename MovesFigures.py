import copy

from Cage import Cage


class MoveFigures:
    def __init__(self, game):
        self.game = game

    def draw(self, possible_moves):
        for move in possible_moves:
            self.game.dict_cages[move].color = "green"

    def get_attack_cages(self, color, figure):
        attack_cages = set()
        for cage in self.game.dict_cages.values():
            if cage.figure is not None and cage.figure.color != color:
                for cord in figure.get_moves(cage.coordinate, cage):
                    attack_cages.add(cord)
        return attack_cages

    def is_check(self, color, figure):
        king = [x.coordinate for x in self.game.dict_cages.values() if x.figure is not None and
                x.figure.name == "king" and x.figure.color == color]
        return king[0] in self.get_attack_cages(color, figure) if len(king) > 0 else False

    def get_possible_defense_moves(self, color, figure):
        possible_defense_moves = set()

        # Получаем все фигуры заданного цвета
        pieces = [cage for cage in self.game.dict_cages.values() if cage.figure is not None and
                  cage.figure.color == color]

        # Для каждой фигуры получаем возможные ходы атаки
        for piece in pieces:
            attack_moves = figure.get_moves(piece.coordinate, piece)

            # Проверяем, есть ли ходы для защиты от атаки
            for move in attack_moves:

                current_cage = self.game.dict_cages[piece.coordinate]
                target_cage = self.game.dict_cages[move]

                self.game.dict_cages[move] = current_cage
                self.game.dict_cages[piece.coordinate] = target_cage

                if not self.is_check(color, figure):
                    possible_defense_moves.add(move)

                self.game.dict_cages[move] = target_cage
                self.game.dict_cages[piece.coordinate] = current_cage

        return possible_defense_moves
