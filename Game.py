import tkinter as tk
from Cage import Cage
from Pawn import Pawn
from Rook import Rook
from Horse import Horse
from Elephant import Elephant
from Queen import Queen
from King import King
from MovesFigures import MoveFigures
from Player import Player

class Game:
    def __init__(self, root, images, canvas, square_size, diffy, diffx):
        self.root = root
        self.current = None
        self.images = images
        self.square_size = square_size
        self.diffy = diffy
        self.diffx = diffx
        self.canvas = canvas
        self.canvas.bind('<Button-1>', self.on_click)
        self.move_figures = MoveFigures(self)
        self.white_player = Player()
        self.black_player = Player()
        self.dict_cages = {
            (0, 1):  Cage("black", (0, 1), Pawn("white", self.move_figures, self, (0, 1))),
            (1, 1):  Cage("white", (1, 1), Pawn("white", self.move_figures, self, (1, 1))),
            (2, 1):  Cage("black", (2, 1), Pawn("white", self.move_figures, self, (2, 1))),
            (3, 1):  Cage("white", (3, 1), Pawn("white", self.move_figures, self, (3, 1))),
            (4, 1):  Cage("black", (4, 1), Pawn("white", self.move_figures, self, (4, 1))),
            (5, 1):  Cage("white", (5, 1), Pawn("white", self.move_figures, self, (5, 1))),
            (6, 1):  Cage("black", (6, 1), Pawn("white", self.move_figures, self, (6, 1))),
            (7, 1):  Cage("white", (7, 1), Pawn("white", self.move_figures, self, (7, 1))),

            (0, 0): Cage("white", (0, 0), Rook("white", self.move_figures, self, (0, 0))),
            (1, 0): Cage("black", (1, 0), Horse("white", self.move_figures, self, (1, 0))),
            (2, 0): Cage("white", (2, 0), Elephant("white", self.move_figures, self, (2, 0))),
            (3, 0): Cage("black", (3, 0), Queen("white", self.move_figures, self, (3, 0))),
            (4, 0): Cage("white", (4, 0), King("white", self.move_figures, self, (4, 0))),
            (5, 0): Cage("black", (5, 0), Elephant("white", self.move_figures, self, (5, 0))),
            (6, 0): Cage("white", (6, 0), Horse("white", self.move_figures, self, (6, 0))),
            (7, 0): Cage("black", (7, 0), Rook("white", self.move_figures, self, (7, 0))),

            (0, 6): Cage("white", (0, 6), Pawn("black", self.move_figures, self, (0, 6))),
            (1, 6): Cage("black", (1, 6), Pawn("black", self.move_figures, self, (1, 6))),
            (2, 6): Cage("white", (2, 6), Pawn("black", self.move_figures, self, (2, 6))),
            (3, 6): Cage("black", (3, 6), Pawn("black", self.move_figures, self, (3, 6))),
            (4, 6): Cage("white", (4, 6), Pawn("black", self.move_figures, self, (4, 6))),
            (5, 6): Cage("black", (5, 6), Pawn("black", self.move_figures, self, (5, 6))),
            (6, 6): Cage("white", (6, 6), Pawn("black", self.move_figures, self, (6, 6))),
            (7, 6): Cage("black", (7, 6), Pawn("black", self.move_figures, self, (7, 6))),

            (0, 7): Cage("black", (0, 7), Rook("black", self.move_figures, self, (0, 7))),
            (1, 7): Cage("white", (1, 7), Horse("black", self.move_figures, self, (1, 7))),
            (2, 7): Cage("black", (2, 7), Elephant("black", self.move_figures, self, (2, 7))),
            (3, 7): Cage("white", (3, 7), Queen("black", self.move_figures, self, (3, 7))),
            (4, 7): Cage("black", (4, 7), King("black", self.move_figures, self, (4, 7))),
            (5, 7): Cage("white", (5, 7), Elephant("black", self.move_figures, self, (5, 7))),
            (6, 7): Cage("black", (6, 7), Horse("black", self.move_figures, self, (6, 7))),
            (7, 7): Cage("white", (7, 7), Rook("black", self.move_figures, self, (7, 7)))}
        
        for cage in self.dict_cages.values():
            if cage.figure.color == "white":
                self.white_player.add_figure(cage.figure)
            else:
                self.black_player.add_figure(cage.figure)

        for i in range(8):
            for j in range(8):
                if (i, j) not in self.dict_cages:
                    self.dict_cages[(i, j)] = Cage(["white", "black"][(i + j) % 2], (i, j))
        self.draw_chessboard(self.dict_cages)

    def on_click(self, event):
        coordinate = ((event.x - self.diffx) // self.square_size, (event.y - self.diffy) // self.square_size)
        cage = self.dict_cages[coordinate]

        self.draw_chessboard(self.dict_cages)

        if cage.color == "green" and self.current is not None:
            # Переместить фигуру на выбранную клетку
            source_coordinate, source_cage = self.current
            if source_cage.figure.color == "white":
                for figure in self.white_player.figures:
                    if figure.name == source_cage.figure.name:
                        figure.coordinate = coordinate
                        break
            else:
                for figure in self.black_player.figures:
                    if figure.name == source_cage.figure.name:
                        figure.coordinate = coordinate
                        break
            source_cage.figure.coordinate = coordinate
            self.dict_cages[coordinate].figure = source_cage.figure
            self.dict_cages[source_coordinate].figure = None

            self.current = None
            self.full()
        elif cage.color != "green" and cage.figure is not None:
            self.full()
            self.current = (coordinate, cage)
            cage.figure.moves(coordinate, cage)

        self.draw_chessboard(self.dict_cages)

    def full(self):
        for i in range(8):
            for j in range(8):
                    self.dict_cages[(i, j)].color = ["white", "black"][(i + j) % 2]

    def draw_chessboard(self, dict_cages):
        for cage in self.dict_cages.values():
            self.canvas.create_rectangle(cage.coordinate[0] * self.square_size + self.diffx,
                                        cage.coordinate[1] * self.square_size + self.diffy,
                                        cage.coordinate[0] * self.square_size + self.square_size + self.diffx,
                                        cage.coordinate[1] * self.square_size + self.square_size + self.diffy,
                                           fill= dict_cages[cage.coordinate].color)
            if dict_cages[cage.coordinate].figure is not None:
                self.canvas.create_image(cage.coordinate[0] * self.square_size + self.diffx - 2,
                    cage.coordinate[1] * self.square_size + self.diffy - 20,
                    anchor=tk.NW,image=self.images[f"{dict_cages[cage.coordinate].figure.color}_{dict_cages[cage.coordinate].figure.name}"])