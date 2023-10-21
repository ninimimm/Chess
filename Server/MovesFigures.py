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

    def is_check(self, enemy_to_king, dict_cages):
        for enemy_figure in enemy_to_king:
            #print("enemy", enemy_figure.name)
            #print(enemy_figure.get_moves(enemy_figure.coordinate, dict_cages[enemy_figure.coordinate], dict_cages))
            for cord in enemy_figure.get_moves(enemy_figure.coordinate, dict_cages[enemy_figure.coordinate], dict_cages):
                if cord == self.king.coordinate:
                    return True
        return False

    def get_possible_defense_moves(self, color, dict_cages):
        possible_defense_moves = set()
        enemy_to_king = []
        self.enemy_figures = []
        for cage in dict_cages.values():
            if cage.figure is not None:
                if cage.figure.color == color:
                    if "king" in cage.figure.name:
                        self.king = cage.figure
                else:
                    self.enemy_figures.append(cage.figure)
        # if color == "white":
        #     self.our_figures = self.game.white_player.figures
        #     self.enemy_figures = self.game.black_player.figures
        # else:
        #     self.our_figures = self.game.black_player.figures
        #     self.enemy_figures = self.game.white_player.figures
        # if self.game.current[1].figure.name == "king":
        #     enemy_to_king = self.enemy_figures
        # else:
        #     for figure in self.enemy_figures:
        #         if self.our_figures[0].coordinate in figure.get_moves(figure.coordinate, dict_cages[figure.coordinate], dict_cages):
        #             enemy_to_king.append(figure)
        #print("enemy_to_king", enemy_to_king)
        piece = dict_cages[self.game.current[1].figure.coordinate].figure
        for move in piece.get_moves(piece.coordinate, dict_cages[piece.coordinate], dict_cages):
            start_cord = piece.coordinate
            finish_figure = dict_cages[move].figure
            piece.coordinate = move
            dict_cages[move].figure = piece
            dict_cages[start_cord].figure = None
            if not self.is_check(self.enemy_figures, dict_cages):
                possible_defense_moves.add(move)

            piece.coordinate = start_cord
            dict_cages[start_cord].figure = piece
            dict_cages[move].figure = finish_figure
        #print(possible_defense_moves)
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
            if len(f"{dict_copy[key]}") == 8: str += f"    {self.get_figure(dict_copy[key].figure)}    "
            else: str += f"{dict_copy[key]}  "
        print(str)

    def get_figure(self, figure):
        if figure is None: return " . "
        if figure.name == "p": return '\u2659'
        if figure.name == "r": return '\u2656'
        if figure.name == "h": return '\u2658'
        if figure.name == "q": return '\u2655'
        if figure.name == "k": return '\u2654'
        if figure.name == "e": return '\u2657'