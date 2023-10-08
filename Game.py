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
        self.current_player = 0
        self.move_figures = MoveFigures(self)
        self.white_player = Player()
        self.black_player = Player()
        self.squares = [[self.canvas.create_rectangle(i * self.square_size + self.diffx,
                                            j * self.square_size + self.diffy,
                                            i * self.square_size + self.square_size + self.diffx,
                                            j * self.square_size + self.square_size + self.diffy,
                                               fill= ["white", "black"][(i + j) % 2]) for i in range(8)] for j in range(8)]
        self.dict_cages = {
            (4, 0): Cage("white", (4, 0), King("white", self.move_figures, self, (4, 0),
                                               self.canvas.create_image(4 * self.square_size + self.diffx - 2,
                                                                        0 * self.square_size + self.diffy - 20,
                                                                        anchor=tk.NW,
                                                                        image=self.images[f"white_king"]))),
            (0, 1): Cage("black", (0, 1), Pawn("white", self.move_figures, self, (0, 1),
                                               self.canvas.create_image(0 * self.square_size + self.diffx - 2,
                                                                        1 * self.square_size + self.diffy - 20,
                                                                        anchor=tk.NW,
                                                                        image=self.images[f"white_pawn"]))),
            (1, 1): Cage("white", (1, 1), Pawn("white", self.move_figures, self, (1, 1),
                                               self.canvas.create_image(1 * self.square_size + self.diffx - 2,
                                                                        1 * self.square_size + self.diffy - 20,
                                                                        anchor=tk.NW,
                                                                        image=self.images[f"white_pawn"]))),
            (2, 1): Cage("black", (2, 1), Pawn("white", self.move_figures, self, (2, 1),
                                               self.canvas.create_image(2 * self.square_size + self.diffx - 2,
                                                                        1 * self.square_size + self.diffy - 20,
                                                                        anchor=tk.NW,
                                                                        image=self.images[f"white_pawn"]))),
            (3, 1): Cage("white", (3, 1), Pawn("white", self.move_figures, self, (3, 1),
                                               self.canvas.create_image(3 * self.square_size + self.diffx - 2,
                                                                        1 * self.square_size + self.diffy - 20,
                                                                        anchor=tk.NW,
                                                                        image=self.images[f"white_pawn"]))),
            (4, 1): Cage("black", (4, 1), Pawn("white", self.move_figures, self, (4, 1),
                                               self.canvas.create_image(4 * self.square_size + self.diffx - 2,
                                                                        1 * self.square_size + self.diffy - 20,
                                                                        anchor=tk.NW,
                                                                        image=self.images[f"white_pawn"]))),
            (5, 1): Cage("white", (5, 1), Pawn("white", self.move_figures, self, (5, 1),
                                               self.canvas.create_image(5 * self.square_size + self.diffx - 2,
                                                                        1 * self.square_size + self.diffy - 20,
                                                                        anchor=tk.NW,
                                                                        image=self.images[f"white_pawn"]))),
            (6, 1): Cage("black", (6, 1), Pawn("white", self.move_figures, self, (6, 1),
                                               self.canvas.create_image(6 * self.square_size + self.diffx - 2,
                                                                        1 * self.square_size + self.diffy - 20,
                                                                        anchor=tk.NW,
                                                                        image=self.images[f"white_pawn"]))),
            (7, 1): Cage("white", (7, 1), Pawn("white", self.move_figures, self, (7, 1),
                                               self.canvas.create_image(7 * self.square_size + self.diffx - 2,
                                                                        1 * self.square_size + self.diffy - 20,
                                                                        anchor=tk.NW,
                                                                        image=self.images[f"white_pawn"]))),

            (0, 0): Cage("white", (0, 0), Rook("white", self.move_figures, self, (0, 0),
                                               self.canvas.create_image(0 * self.square_size + self.diffx - 2,
                                                                        0 * self.square_size + self.diffy - 20,
                                                                        anchor=tk.NW,
                                                                        image=self.images[f"white_rook"]))),
            (1, 0): Cage("black", (1, 0), Horse("white", self.move_figures, self, (1, 0),
                                                self.canvas.create_image(1 * self.square_size + self.diffx - 2,
                                                                         0 * self.square_size + self.diffy - 20,
                                                                         anchor=tk.NW,
                                                                         image=self.images[f"white_horse"]))),
            (2, 0): Cage("white", (2, 0), Elephant("white", self.move_figures, self, (2, 0),
                                                   self.canvas.create_image(2 * self.square_size + self.diffx - 2,
                                                                            0 * self.square_size + self.diffy - 20,
                                                                            anchor=tk.NW,
                                                                            image=self.images[f"white_elephant"]))),
            (3, 0): Cage("black", (3, 0), Queen("white", self.move_figures, self, (3, 0),
                                                self.canvas.create_image(3 * self.square_size + self.diffx - 2,
                                                                         0 * self.square_size + self.diffy - 20,
                                                                         anchor=tk.NW,
                                                                         image=self.images[f"white_queen"]))),

            (5, 0): Cage("black", (5, 0), Elephant("white", self.move_figures, self, (5, 0),
                                                   self.canvas.create_image(5 * self.square_size + self.diffx - 2,
                                                                            0 * self.square_size + self.diffy - 20,
                                                                            anchor=tk.NW,
                                                                            image=self.images[f"white_elephant"]))),
            (6, 0): Cage("white", (6, 0), Horse("white", self.move_figures, self, (6, 0),
                                                self.canvas.create_image(6 * self.square_size + self.diffx - 2,
                                                                         0 * self.square_size + self.diffy - 20,
                                                                         anchor=tk.NW,
                                                                         image=self.images[f"white_horse"]))),
            (7, 0): Cage("black", (7, 0), Rook("white", self.move_figures, self, (7, 0),
                                               self.canvas.create_image(7 * self.square_size + self.diffx - 2,
                                                                        0 * self.square_size + self.diffy - 20,
                                                                        anchor=tk.NW,
                                                                        image=self.images[f"white_rook"]))),

            (4, 7): Cage("black", (4, 7), King("black", self.move_figures, self, (4, 7),
                                               self.canvas.create_image(4 * self.square_size + self.diffx - 2,
                                                                        7 * self.square_size + self.diffy - 20,
                                                                        anchor=tk.NW,
                                                                        image=self.images[f"black_king"]))),
            (0, 6): Cage("white", (0, 6), Pawn("black", self.move_figures, self, (0, 6),
                                               self.canvas.create_image(0 * self.square_size + self.diffx - 2,
                                                                        6 * self.square_size + self.diffy - 20,
                                                                        anchor=tk.NW,
                                                                        image=self.images[f"black_pawn"]))),
            (1, 6): Cage("black", (1, 6), Pawn("black", self.move_figures, self, (1, 6),
                                               self.canvas.create_image(1 * self.square_size + self.diffx - 2,
                                                                        6 * self.square_size + self.diffy - 20,
                                                                        anchor=tk.NW,
                                                                        image=self.images[f"black_pawn"]))),
            (2, 6): Cage("white", (2, 6), Pawn("black", self.move_figures, self, (2, 6),
                                               self.canvas.create_image(2 * self.square_size + self.diffx - 2,
                                                                        6 * self.square_size + self.diffy - 20,
                                                                        anchor=tk.NW,
                                                                        image=self.images[f"black_pawn"]))),
            (3, 6): Cage("black", (3, 6), Pawn("black", self.move_figures, self, (3, 6),
                                               self.canvas.create_image(3 * self.square_size + self.diffx - 2,
                                                                        6 * self.square_size + self.diffy - 20,
                                                                        anchor=tk.NW,
                                                                        image=self.images[f"black_pawn"]))),
            (4, 6): Cage("white", (4, 6), Pawn("black", self.move_figures, self, (4, 6),
                                               self.canvas.create_image(4 * self.square_size + self.diffx - 2,
                                                                        6 * self.square_size + self.diffy - 20,
                                                                        anchor=tk.NW,
                                                                        image=self.images[f"black_pawn"]))),
            (5, 6): Cage("black", (5, 6), Pawn("black", self.move_figures, self, (5, 6),
                                               self.canvas.create_image(5 * self.square_size + self.diffx - 2,
                                                                        6 * self.square_size + self.diffy - 20,
                                                                        anchor=tk.NW,
                                                                        image=self.images[f"black_pawn"]))),
            (6, 6): Cage("white", (6, 6), Pawn("black", self.move_figures, self, (6, 6),
                                               self.canvas.create_image(6 * self.square_size + self.diffx - 2,
                                                                        6 * self.square_size + self.diffy - 20,
                                                                        anchor=tk.NW,
                                                                        image=self.images[f"black_pawn"]))),
            (7, 6): Cage("black", (7, 6), Pawn("black", self.move_figures, self, (7, 6),
                                               self.canvas.create_image(7 * self.square_size + self.diffx - 2,
                                                                        6 * self.square_size + self.diffy - 20,
                                                                        anchor=tk.NW,
                                                                        image=self.images[f"black_pawn"]))),

            (0, 7): Cage("black", (0, 7), Rook("black", self.move_figures, self, (0, 7),
                                               self.canvas.create_image(0 * self.square_size + self.diffx - 2,
                                                                        7 * self.square_size + self.diffy - 20,
                                                                        anchor=tk.NW,
                                                                        image=self.images[f"black_rook"]))),
            (1, 7): Cage("white", (1, 7), Horse("black", self.move_figures, self, (1, 7),
                                                self.canvas.create_image(1 * self.square_size + self.diffx - 2,
                                                                         7 * self.square_size + self.diffy - 20,
                                                                         anchor=tk.NW,
                                                                         image=self.images[f"black_horse"]))),
            (2, 7): Cage("black", (2, 7), Elephant("black", self.move_figures, self, (2, 7),
                                                   self.canvas.create_image(2 * self.square_size + self.diffx - 2,
                                                                            7 * self.square_size + self.diffy - 20,
                                                                            anchor=tk.NW,
                                                                            image=self.images[f"black_elephant"]))),
            (3, 7): Cage("white", (3, 7), Queen("black", self.move_figures, self, (3, 7),
                                                self.canvas.create_image(3 * self.square_size + self.diffx - 2,
                                                                         7 * self.square_size + self.diffy - 20,
                                                                         anchor=tk.NW,
                                                                         image=self.images[f"black_queen"]))),

            (5, 7): Cage("white", (5, 7), Elephant("black", self.move_figures, self, (5, 7),
                                                   self.canvas.create_image(5 * self.square_size + self.diffx - 2,
                                                                            7 * self.square_size + self.diffy - 20,
                                                                            anchor=tk.NW,
                                                                            image=self.images[f"black_elephant"]))),
            (6, 7): Cage("black", (6, 7), Horse("black", self.move_figures, self, (6, 7),
                                                self.canvas.create_image(6 * self.square_size + self.diffx - 2,
                                                                         7 * self.square_size + self.diffy - 20,
                                                                         anchor=tk.NW,
                                                                         image=self.images[f"black_horse"]))),
            (7, 7): Cage("white", (7, 7), Rook("black", self.move_figures, self, (7, 7),
                                               self.canvas.create_image(7 * self.square_size + self.diffx - 2,
                                                                        7 * self.square_size + self.diffy - 20,
                                                                        anchor=tk.NW,
                                                                        image=self.images[f"black_rook"])))}

        for cage in self.dict_cages.values():
            if cage.figure.color == "white":
                self.white_player.add_figure(cage.figure)
            else:
                self.black_player.add_figure(cage.figure)

        for i in range(8):
            for j in range(8):
                if (i, j) not in self.dict_cages:
                    self.dict_cages[(i, j)] = Cage(["white", "black"][(i + j) % 2], (i, j))

    def on_click(self, event):
        coordinate = ((event.x - self.diffx) // self.square_size, (event.y - self.diffy) // self.square_size)
        cage = self.dict_cages[coordinate]
        if cage.color == "green" and self.current is not None:
            source_coordinate, source_cage = self.current
            if source_cage.figure.color == "white":
                if self.dict_cages[coordinate].figure is not None:
                    self.canvas.move(self.dict_cages[coordinate].figure.image, 10000, 10000)
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
                    self.canvas.move(self.dict_cages[coordinate].figure.image, 10000, 10000)
                    for i in range(len(self.white_player.figures)):
                        if self.white_player.figures[i].coordinate == coordinate:
                            self.white_player.figures.pop(i)
                            break
                for figure in self.black_player.figures:
                    if figure.name == source_cage.figure.name and figure.coordinate == source_cage.figure.coordinate:
                        figure.coordinate = coordinate
                        break
            self.fill()

            source_cage.figure.coordinate = coordinate
            self.dict_cages[coordinate].figure = source_cage.figure
            self.dict_cages[source_coordinate].figure = None
            self.canvas.move(self.dict_cages[coordinate].figure.image,
                             (coordinate[0] - source_coordinate[0]) * self.square_size,
                             (coordinate[1] - source_coordinate[1]) * self.square_size)
            self.current = None
            self.current_player = (self.current_player + 1) % 2

        elif cage.color != "green" and cage.figure is not None and cage.figure.color == ["white", "black"][self.current_player]:
            self.current = (coordinate, cage)
            self.fill()
            cage.figure.moves(coordinate, cage)

    def fill(self):
        for i in range(8):
            for j in range(8):
                color = ["white", "black"][(i + j) % 2]
                self.canvas.itemconfig(self.squares[i][j], fill = color)
                self.dict_cages[(i, j)].color = color
