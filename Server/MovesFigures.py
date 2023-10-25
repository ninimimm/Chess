from colorama import Style, init
init(autoreset=True)

class MoveFigures:
    def __init__(self, game):
        self.game = game
        self.king = None
        self.enemy_figures = []
        self.dict_figure_moves = {}

    def draw(self, possible_moves): # pragma: no cover
        for move in possible_moves:
            self.game.dict_cages[move].color = "green"

    def is_check(self, args):
        enemy_to_king, dict_cages, tuple_coordinate = args
        for enemy_figure in enemy_to_king:
            args = enemy_figure, dict_cages, tuple_coordinate
            for cord in self.get_enemy_figure_moves(args):
                if cord == self.king.coordinate:
                    return True
        return False

    def get_enemy_figure_moves(self, args):
        enemy_figure, dict_cages, tuple_coordinate = args
        if enemy_figure.name not in self.dict_figure_moves or \
            any(any(cord in value for value in self.dict_figure_moves[enemy_figure.name].values()) for cord in tuple_coordinate):
            enemy_figure_moves = enemy_figure.get_moves(enemy_figure.coordinate,
                                                        dict_cages[enemy_figure.coordinate], dict_cages)
            self.dict_figure_moves[enemy_figure.name] = enemy_figure_moves.copy()
            return enemy_figure_moves
        return self.dict_figure_moves[enemy_figure.name]

    def get_enemy_figures(self, dict_cages, color):
        enemy_figures = []
        for cage in dict_cages.values():
            if cage.figure is not None:
                if cage.figure.color == color:
                    if "king" in cage.figure.name:
                        self.king = cage.figure
                else:
                    enemy_figures.append(cage.figure)
        return enemy_figures

    def get_possible_defense_moves(self, color, dict_cages):
        possible_defense_moves = set()
        self.enemy_figures = self.get_enemy_figures(dict_cages, color)
        piece = dict_cages[self.game.current[1].figure.coordinate].figure
        for move in piece.get_moves(piece.coordinate, dict_cages[piece.coordinate], dict_cages):
            start_cord = piece.coordinate
            finish_figure = dict_cages[move].figure
            piece.coordinate = move
            dict_cages[move].figure = piece
            dict_cages[start_cord].figure = None
            args = self.enemy_figures, dict_cages, (start_cord, move)
            if not self.is_check(args):
                possible_defense_moves.add(move)
            piece.coordinate = start_cord
            dict_cages[start_cord].figure = piece
            dict_cages[move].figure = finish_figure
        return possible_defense_moves


    def print_dict_copy(self, dict_copy): # pragma: no cover
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

    def get_figure(self, figure): # pragma: no cover
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

