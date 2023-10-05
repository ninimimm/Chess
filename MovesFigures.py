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

    def draw(self, possible_moves):
        for move in possible_moves:
            self.game.dict_cages[move].color = "green"

    def copy_cage(self, cage):
        return Cage(cage.color, cage.coordinate, self.copy_figure(cage.figure))

    def copy_figure(self, figure):
        if figure is None: return None
        match figure.name:
            case "pawn":
                return Pawn(figure.color, figure.move_figures, figure.game, figure.coordinate)
            case "rook":
                return Rook(figure.color, figure.move_figures, figure.game, figure.coordinate)
            case "horse":
                return Horse(figure.color, figure.move_figures, figure.game, figure.coordinate)
            case "elephant":
                return Elephant(figure.color, figure.move_figures, figure.game, figure.coordinate)
            case "queen":
                return Queen(figure.color, figure.move_figures, figure.game, figure.coordinate)
            case "king":
                return King(figure.color, figure.move_figures, figure.game, figure.coordinate)

    def is_check(self, color):
        our_figures, enemy_figures, king = [], [], None
        if color == "white":
            our_figures = self.game.white_player.figures
            enemy_figures = self.game.black_player.figures
        else:
            our_figures = self.game.black_player.figures
            enemy_figures = self.game.white_player.figures

        for our_figure in our_figures:
            if our_figure.name == "king":
                king = our_figure
                break

        p = []
        for enemy_figure in enemy_figures:
            for cord in enemy_figure.get_moves(enemy_figure.coordinate, self.game.dict_cages[enemy_figure.coordinate]):
                p.append(cord)
                if cord == king.coordinate:
                    return True
        return False

    def get_possible_defense_moves(self, color):
        possible_defense_moves = set()
        pieces = (self.game.white_player.figures if color == "white" else self.game.black_player.figures)

        for piece in pieces:
            if self.game.current[1].figure.name == "king" and piece.name != "king":
               continue
            for move in piece.get_moves(piece.coordinate, self.game.dict_cages[piece.coordinate]):
                self.print_dict_copy(self.game.dict_cages)
                start_cord = piece.coordinate
                finish_figure = self.game.dict_cages[move].figure
                piece.coordinate = move
                self.game.dict_cages[move].figure = piece
                self.game.dict_cages[start_cord].figure = None
                self.print_dict_copy(self.game.dict_cages)
                if not self.is_check(color):
                    possible_defense_moves.add(move)
                piece.coordinate = start_cord
                self.game.dict_cages[start_cord].figure = piece
                self.game.dict_cages[move].figure = finish_figure
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