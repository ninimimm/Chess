import copy
from Pawn import Pawn
from Horse import Horse
from Rook import Rook
from Elephant import Elephant
from Queen import Queen
from King import King
from Cage import Cage

class MoveFigures:
    def __init__(self, game):
        self.game = game
        self.our_figures = []
        self.enemy_figures = []

    def draw(self, possible_moves):
        for move in possible_moves:
            self.game.dict_cages[move].color = "green"

    def copy_cage(self, cage):
        return Cage(cage.color, cage.coordinate, self.copy_figure(cage.figure))

    def copy_figure(self, figure):
        if figure is None: return None
        if figure.name == "pawn":
            return Pawn(figure.color, figure.move_figures, figure.game, figure.coordinate)
        elif figure.name == "rook":
            return Rook(figure.color, figure.move_figures, figure.game, figure.coordinate)
        elif figure.name == "horse":
            return Horse(figure.color, figure.move_figures, figure.game, figure.coordinate)
        elif figure.name == "elephant":
            return Elephant(figure.color, figure.move_figures, figure.game, figure.coordinate)
        elif figure.name == "queen":
            return Queen(figure.color, figure.move_figures, figure.game, figure.coordinate)
        elif figure.name == "king":
            return King(figure.color, figure.move_figures, figure.game, figure.coordinate)

    def is_check(self, enemy_to_king):
        king = self.our_figures[0]
        for enemy_figure in enemy_to_king:
            for cord in enemy_figure.get_moves(enemy_figure.coordinate, self.game.dict_cages[enemy_figure.coordinate]):
                if cord == king.coordinate:
                    return True
        return False

    def get_possible_defense_moves(self, color):
        possible_defense_moves = set()
        enemy_to_king = []
        if color == "white":
            self.our_figures = self.game.white_player.figures
            self.enemy_figures = self.game.black_player.figures
        else:
            self.our_figures = self.game.black_player.figures
            self.enemy_figures = self.game.white_player.figures
        print(self.enemy_figures)
        if self.game.current[1].figure.name == "king":
            enemy_to_king = self.enemy_figures
        else:
            for figure in self.enemy_figures:
                if self.our_figures[0].coordinate in figure.get_moves(figure.coordinate, self.game.dict_cages[figure.coordinate]):
                    enemy_to_king.append(figure)
            print(enemy_to_king, "enemy_to_king")

        piece = self.game.dict_cages[self.game.current[1].figure.coordinate].figure
        for move in piece.get_moves(piece.coordinate, self.game.dict_cages[piece.coordinate]):
            start_cord = piece.coordinate
            finish_figure = self.game.dict_cages[move].figure
            piece.coordinate = move
            self.game.dict_cages[move].figure = piece
            self.game.dict_cages[start_cord].figure = None
            print(self.is_check(enemy_to_king))
            if not self.is_check(enemy_to_king):
                possible_defense_moves.add(move)

            piece.coordinate = start_cord
            self.game.dict_cages[start_cord].figure = piece
            self.game.dict_cages[move].figure = finish_figure
        print(possible_defense_moves)
        return possible_defense_moves

    def print_dict_copy(self, dict_copy):
        keys = []
        for key in dict_copy.keys():
            keys.append(key)
        keys = sorted(keys, key=lambda x: x[1])
        count = 0
        str = ""
        for key in keys:
            if count % 8 == 0:
                print(str)
                str = ""
            count += 1
            if len(f"{dict_copy[key]}") == 8: str += f"    {dict_copy[key]}    "
            else: str += f"{dict_copy[key]}  "
        print(str)