import copy

from Cage import Cage
from Figures.Pawn import Pawn
from Figures.Rook import Rook
from Figures.Horse import Horse
from Figures.Elephant import Elephant
from Figures.Queen import Queen
from Figures.King import King
from MovesFigures import MoveFigures
from Player import Player


class Game:
    def __init__(self, square_size, diffy, diffx):
        self.last_move = None
        self.players_ip = {}
        self.index_white_pawn = 0
        self.index_black_pawn = 0
        self.index_white_rook = 0
        self.index_black_rook = 0
        self.index_white_horse = 0
        self.index_black_horse = 0
        self.index_white_elephant = 0
        self.index_black_elephant = 0
        self.index_black_queen = 0
        self.index_white_queen = 0
        self.current = None
        self.square_size = square_size
        self.diffy = diffy
        self.diffx = diffx
        self.current_player = 0
        self.move_figures = MoveFigures(self)
        self.white_player = Player()
        self.black_player = Player()
        self.ready = True
        self.figure_buttons = []
        self.dict_cages = {
            (3, 0): Cage("white", (3, 0), King("white", self.move_figures, self, (3, 0), 0)),
            (0, 1): Cage("black", (0, 1), Pawn("white", self.move_figures, self, (0, 1), self.index_white_pawn)),
            (1, 1): Cage("white", (1, 1), Pawn("white", self.move_figures, self, (1, 1), self.index_white_pawn)),
            (2, 1): Cage("black", (2, 1), Pawn("white", self.move_figures, self, (2, 1), self.index_white_pawn)),
            (3, 1): Cage("white", (3, 1), Pawn("white", self.move_figures, self, (3, 1), self.index_white_pawn)),
            (4, 1): Cage("black", (4, 1), Pawn("white", self.move_figures, self, (4, 1), self.index_white_pawn)),
            (5, 1): Cage("white", (5, 1), Pawn("white", self.move_figures, self, (5, 1), self.index_white_pawn)),
            (6, 1): Cage("black", (6, 1), Pawn("white", self.move_figures, self, (6, 1), self.index_white_pawn)),
            (7, 1): Cage("white", (7, 1), Pawn("white", self.move_figures, self, (7, 1), self.index_white_pawn)),

            (0, 0): Cage("white", (0, 0), Rook("white", self.move_figures, self, (0, 0), self.index_white_rook)),
            (1, 0): Cage("black", (1, 0), Horse("white", self.move_figures, self, (1, 0), self.index_white_horse)),
            (2, 0): Cage("white", (2, 0),
                         Elephant("white", self.move_figures, self, (2, 0), self.index_white_elephant)),
            (4, 0): Cage("black", (4, 0), Queen("white", self.move_figures, self, (4, 0), self.index_white_queen)),

            (5, 0): Cage("black", (5, 0),
                         Elephant("white", self.move_figures, self, (5, 0), self.index_white_elephant)),
            (6, 0): Cage("white", (6, 0), Horse("white", self.move_figures, self, (6, 0), self.index_white_horse)),
            (7, 0): Cage("black", (7, 0), Rook("white", self.move_figures, self, (7, 0), self.index_white_rook)),

            (3, 7): Cage("black", (3, 7), King("black", self.move_figures, self, (3, 7), 0)),
            (0, 6): Cage("white", (0, 6), Pawn("black", self.move_figures, self, (0, 6), self.index_black_pawn)),
            (1, 6): Cage("black", (1, 6), Pawn("black", self.move_figures, self, (1, 6), self.index_black_pawn)),
            (2, 6): Cage("white", (2, 6), Pawn("black", self.move_figures, self, (2, 6), self.index_black_pawn)),
            (3, 6): Cage("black", (3, 6), Pawn("black", self.move_figures, self, (3, 6), self.index_black_pawn)),
            (4, 6): Cage("white", (4, 6), Pawn("black", self.move_figures, self, (4, 6), self.index_black_pawn)),
            (5, 6): Cage("black", (5, 6), Pawn("black", self.move_figures, self, (5, 6), self.index_black_pawn)),
            (6, 6): Cage("white", (6, 6), Pawn("black", self.move_figures, self, (6, 6), self.index_black_pawn)),
            (7, 6): Cage("black", (7, 6), Pawn("black", self.move_figures, self, (7, 6), self.index_black_pawn)),

            (0, 7): Cage("black", (0, 7), Rook("black", self.move_figures, self, (0, 7), self.index_black_rook)),
            (1, 7): Cage("white", (1, 7), Horse("black", self.move_figures, self, (1, 7), self.index_black_horse)),
            (2, 7): Cage("black", (2, 7),
                         Elephant("black", self.move_figures, self, (2, 7), self.index_black_elephant)),
            (4, 7): Cage("white", (4, 7), Queen("black", self.move_figures, self, (4, 7), self.index_black_queen)),

            (5, 7): Cage("white", (5, 7),
                         Elephant("black", self.move_figures, self, (5, 7), self.index_black_elephant)),
            (6, 7): Cage("black", (6, 7), Horse("black", self.move_figures, self, (6, 7), self.index_black_horse)),
            (7, 7): Cage("white", (7, 7), Rook("black", self.move_figures, self, (7, 7), self.index_black_rook))}

        for cage in self.dict_cages.values():
            if cage.figure.color == "white":
                self.white_player.add_figure(cage.figure)
            else:
                self.black_player.add_figure(cage.figure)

        for i in range(8):
            for j in range(8):
                if (i, j) not in self.dict_cages:
                    self.dict_cages[(i, j)] = Cage(["white", "black"][(i + j) % 2], (i, j))

    def on_click(self, coordinate, address):
        if len(self.players_ip) < 2:
            return

        if self.ready:
            cage = self.dict_cages[coordinate]
            if cage.color == "green" and self.current is not None:
                source_coordinate, source_cage = self.current
                if source_cage.figure.color == "white":
                    if self.dict_cages[coordinate].figure is not None:
                        for i in range(len(self.black_player.figures)):
                            if self.black_player.figures[i].coordinate == coordinate:
                                self.black_player.figures.pop(i)
                                break
                    for figure in self.white_player.figures:
                        if figure.name == source_cage.figure.name and figure.coordinate == source_cage.figure.coordinate:
                            figure.coordinate = coordinate
                            break
                else:
                    if self.dict_cages[coordinate].figure is not None:
                        for i in range(len(self.white_player.figures)):
                            if self.white_player.figures[i].coordinate == coordinate:
                                self.white_player.figures.pop(i)
                                break
                    for figure in self.black_player.figures:
                        if figure.name == source_cage.figure.name and figure.coordinate == source_cage.figure.coordinate:
                            figure.coordinate = coordinate
                            break
                self.fill()

                if self.dict_cages[source_coordinate].figure.name == "king" and\
                        self.dict_cages[source_coordinate].figure.last_move is None:
                    if source_coordinate[0] - coordinate[0] > 1 and source_coordinate[1] == coordinate[1]:
                        self.dict_cages[(0, source_coordinate[1])].figure.coordinate = (2, source_coordinate[1])
                        self.dict_cages[(2, source_coordinate[1])].figure = self.dict_cages[(0, source_coordinate[1])].figure
                        self.dict_cages[(0, source_coordinate[1])].figure = None
                    elif coordinate[0] - source_coordinate[0] > 1 and source_coordinate[1] == coordinate[1]:
                        self.dict_cages[(7, source_coordinate[1])].figure.coordinate = (4, source_coordinate[1])
                        self.dict_cages[(4, source_coordinate[1])].figure = self.dict_cages[(7, source_coordinate[1])].figure
                        self.dict_cages[(7, source_coordinate[1])].figure = None

                if self.dict_cages[source_coordinate].figure.name == "rook" or\
                        self.dict_cages[source_coordinate].figure.name == "king":
                    self.dict_cages[source_coordinate].figure.last_move = source_coordinate

                if self.dict_cages[source_coordinate].figure.name == "pawn" and coordinate[0] != source_coordinate[0]:
                    figure = self.dict_cages[(coordinate[0], source_coordinate[1])].figure
                    if figure is not None and figure.color != self.dict_cages[source_coordinate].figure.color:
                        if figure.color == "white":
                            self.white_player.figures.remove(figure)
                        else:
                            self.black_player.figures.remove(figure)
                        self.dict_cages[(coordinate[0], source_coordinate[1])].figure = None

                source_cage.figure.coordinate = coordinate
                self.dict_cages[coordinate].figure = source_cage.figure
                self.dict_cages[source_coordinate].figure = None
                if self.dict_cages[coordinate].figure.name == "pawn" and (coordinate[1] == 7 or coordinate[1] == 0):
                    self.ready = False
                    return f"choice {self.players_ip[address][0]}"
                self.current = None
                self.current_player = (self.current_player + 1) % 2
                self.move_figures.print_dict_copy(self.dict_cages)
                self.last_move = source_coordinate
            elif cage.color != "green" and cage.figure is not None and self.players_ip[address][1] and cage.figure.color == self.players_ip[address][0]:
                self.current = (coordinate, cage)
                self.fill()
                cage.figure.moves(cage, self.dict_cages)
        return self.get_response(address)

    def get_response(self, address):
        string_cages = ""
        string_figures = ""
        for i in range(8):
            for j in range(8):
                string_cages += f"{self.dict_cages[(j, i)].color} "
                if self.dict_cages[(j, i)].figure is None:
                    string_figures += f"None "
                else:
                    string_figures += f"{self.dict_cages[(j, i)].figure.color}_{self.dict_cages[(j, i)].figure.name}{self.dict_cages[(j, i)].figure.index} "
        figures = string_figures.split()
        print(["white", "black"][self.current_player])
        print(self.get_possible_moves(figures, ["white", "black"][self.current_player]))
        if self.get_possible_moves(figures, ["white", "black"][self.current_player]) != {}:
            return f"{string_cages},{string_figures},{self.players_ip[address][0]}"
        print(self.current_player)
        if self.move_figures.is_check((self.move_figures.get_enemy_figures(self.dict_cages, ["white", "black"][self.current_player]), self.dict_cages, (0, 0))):
            return f"{string_cages},{string_figures},{self.players_ip[address][0]}победа"
        return f"{string_cages},{string_figures},{self.players_ip[address][0]}пат"

    def fill(self): # pragma: no cover
        for i in range(8):
            for j in range(8):
                color = ["white", "black"][(i + j) % 2]
                self.dict_cages[(i, j)].color = color

    def create_figure(self, name, coordinate, address):
        if name == "Queen":
            self.dict_cages[coordinate] = Cage(self.dict_cages[coordinate].color, coordinate,
                Queen(self.players_ip[address][0], self.move_figures, self, coordinate,
                      self.index_black_queen if self.players_ip[address][0] == "black" else self.index_white_queen))
        if name == "Horse":
            self.dict_cages[coordinate] = Cage(self.dict_cages[coordinate].color, coordinate,
                Horse(self.players_ip[address][0], self.move_figures, self, coordinate,
                      self.index_black_horse if self.players_ip[address][0] == "black" else self.index_white_horse))
        if name == "Elephant":
            self.dict_cages[coordinate] = Cage(self.dict_cages[coordinate].color, coordinate,
                Elephant(self.players_ip[address][0], self.move_figures, self, coordinate,
                         self.index_black_elephant if self.players_ip[address][0] == "black" else self.index_white_elephant))
        if name == "Rook":
            self.dict_cages[coordinate] = Cage(self.dict_cages[coordinate].color, coordinate,
                Rook(self.players_ip[address][0], self.move_figures, self, coordinate,
                     self.index_black_rook if self.players_ip[address][0] == "black" else self.index_white_rook))

        if self.players_ip[address][0] == "black":
            for i in range(len(self.black_player.figures)):
                if self.black_player.figures[i].coordinate == coordinate:
                    self.black_player.figures.pop(i)
                    break
            self.black_player.add_figure(self.dict_cages[coordinate].figure)
        else:
            for i in range(len(self.white_player.figures)):
                if self.white_player.figures[i].coordinate == coordinate:
                    self.white_player.figures.pop(i)
                    break
            self.white_player.add_figure(self.dict_cages[coordinate].figure)
        self.current = None
        self.current_player = (self.current_player + 1) % 2
        self.fill()

    def get_figure(self, string, coordinate): # pragma: no cover
        color, name = string.split('_')
        name = name[:-1]
        if name == "queen":
            return Queen(color, self.move_figures, self, coordinate,
                         self.index_white_queen if color == "white" else self.index_black_queen)
        if name == "horse":
            return Horse(color, self.move_figures, self, coordinate,
                         self.index_white_horse if color == "white" else self.index_black_horse)
        if name == "elephant":
            return Elephant(color, self.move_figures, self, coordinate,
                         self.index_white_elephant if color == "white" else self.index_black_elephant)
        if name == "rook":
            return Rook(color, self.move_figures, self, coordinate,
                         self.index_white_rook if color == "white" else self.index_black_rook)
        if name == "pawn":
            return Pawn(color, self.move_figures, self, coordinate,
                         self.index_white_pawn if color == "white" else self.index_black_pawn)
        if name == "king":
            return King(color, self.move_figures, self, coordinate, 0)

    def get_new_dict(self, figures):
        new_dict_cages = {}
        for i in range(8):
            for j in range(8):
                if figures[i * 8 + j] == "None":
                    new_dict_cages[(j, i)] = Cage(["white", "black"][(i + j) % 2], (i, j))
                    continue
                new_dict_cages[(j, i)] = Cage(["white", "black"][(i + j) % 2], (j, i), self.get_figure(figures[i * 8 + j], (j, i)))
        return new_dict_cages

    def get_possible_moves(self, figures, color):
        new_dict_cages = self.get_new_dict(figures)
        dict_name_possible_moves = {}
        for coordinate, cage in new_dict_cages.items():
            if cage.figure is not None and cage.figure.color == color:
                self.current = (coordinate, cage)
                pos = cage.figure.get_possible_moves(cage, new_dict_cages)
                if len(pos) > 0:
                    dict_name_possible_moves[coordinate] = [f"{x[0]} {x[1]}" for x in pos]
                self.current = None
        return dict_name_possible_moves
