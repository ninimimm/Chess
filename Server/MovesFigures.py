from colorama import Fore, Style, init
init(autoreset=True)  # Инициализация colorama
import multiprocessing

from Figures.Pawn import Pawn
from Figures.Horse import Horse
from Figures.Rook import Rook
from Figures.Elephant import Elephant
from Figures.Queen import Queen
from Figures.King import King
from Cage import Cage

class MoveFigures:
    def __init__(self, game):
        self.game = game
        self.king = None
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

    def is_figure_kill_king(self, args):
        figure, dict_cages = args
        if figure is None or dict_cages[figure.coordinate].figure is None: return False
        for cord in figure.get_moves(figure.coordinate, dict_cages[figure.coordinate], dict_cages):
            if cord == self.king.coordinate:
                return True
        return False


    def get_possible_defense_moves(self, color, dict_cages):
        possible_defense_moves = set()
        self.enemy_figures = []
        for cage in dict_cages.values():
            if cage.figure is not None:
                if cage.figure.color == color:
                    if "king" in cage.figure.name:
                        self.king = cage.figure
                else:
                    self.enemy_figures.append(cage.figure)
        piece = dict_cages[self.game.current[1].figure.coordinate].figure
        for move in piece.get_moves(piece.coordinate, dict_cages[piece.coordinate], dict_cages):
            start_cord = piece.coordinate
            finish_figure = dict_cages[move].figure
            piece.coordinate = move
            dict_cages[move].figure = piece
            dict_cages[start_cord].figure = None
            with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p:
                print("считаем")
                results = p.map_async(self.is_figure_kill_king, [(x, dict_cages) for x in self.enemy_figures])
                p.close()
                p.join()
            list_res = results.get()
            if not(True in list_res):
                possible_defense_moves.add(move)

            piece.coordinate = start_cord
            dict_cages[start_cord].figure = piece
            dict_cages[move].figure = finish_figure
        print(possible_defense_moves)
        return possible_defense_moves

    def print_dict_copy(self, dict_copy):
        keys = []
        for key in dict_copy.keys():
            keys.append(key)
        keys = sorted(keys, key=lambda x: (x[1], x[0]))
        count = 0
        str_ = ""
        for key in keys:
            if count % 8 == 0:
                print(str_)
                str_ = ""
            count += 1
            str_ += self.get_figure(dict_copy[key].figure) + " "
        print(str_)

    def get_figure(self, figure):
        if figure is None: return "."

        figures = {
            "pawn_white": '\u265F',
            "rook_white": '\u265C',
            "horse_white": '\u265E',
            "queen_white": '\u265B',
            "king_white": '\u265A',
            "elephant_white": '\u265D',
            "pawn_black": '\u2659',
            "rook_black": '\u2656',
            "horse_black": '\u2658',
            "queen_black": '\u2655',
            "king_black": '\u2654',
            "elephant_black": '\u2657'
        }
        return f"{Style.BRIGHT}{figures[f'{figure.name}_{figure.color}']}{Style.RESET_ALL}"

