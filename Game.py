from Cage import Cage
from Pawn import Pawn
from Rook import Rook
from Horse import Horse
from Elephant import Elephant
from Queen import Queen
from King import King
from MovesFigures import MoveFigures
from Player import Player
from PIL import Image, ImageTk

class Game:
    def __init__(self, square_size, diffy, diffx):
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
            (4, 0): Cage("white", (4, 0), King("white", self.move_figures, self, (4, 0))),
            (0, 1): Cage("black", (0, 1), Pawn("white", self.move_figures, self, (0, 1))),
            (1, 1): Cage("white", (1, 1), Pawn("white", self.move_figures, self, (1, 1))),
            (2, 1): Cage("black", (2, 1), Pawn("white", self.move_figures, self, (2, 1))),
            (3, 1): Cage("white", (3, 1), Pawn("white", self.move_figures, self, (3, 1))),
            (4, 1): Cage("black", (4, 1), Pawn("white", self.move_figures, self, (4, 1))),
            (5, 1): Cage("white", (5, 1), Pawn("white", self.move_figures, self, (5, 1))),
            (6, 1): Cage("black", (6, 1), Pawn("white", self.move_figures, self, (6, 1))),
            (7, 1): Cage("white", (7, 1), Pawn("white", self.move_figures, self, (7, 1))),

            (0, 0): Cage("white", (0, 0), Rook("white", self.move_figures, self, (0, 0))),
            (1, 0): Cage("black", (1, 0), Horse("white", self.move_figures, self, (1, 0))),
            (2, 0): Cage("white", (2, 0), Elephant("white", self.move_figures, self, (2, 0))),
            (3, 0): Cage("black", (3, 0), Queen("white", self.move_figures, self, (3, 0))),

            (5, 0): Cage("black", (5, 0), Elephant("white", self.move_figures, self, (5, 0))),
            (6, 0): Cage("white", (6, 0), Horse("white", self.move_figures, self, (6, 0))),
            (7, 0): Cage("black", (7, 0), Rook("white", self.move_figures, self, (7, 0))),

            (4, 7): Cage("black", (4, 7), King("black", self.move_figures, self, (4, 7))),
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

    def on_click(self, coordinate):
        if self.ready == True:
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

                source_cage.figure.coordinate = coordinate
                self.dict_cages[coordinate].figure = source_cage.figure
                self.dict_cages[source_coordinate].figure = None
                if self.dict_cages[coordinate].figure.name == "pawn" and (coordinate[1] == 7 or coordinate[1] == 0):
                    #self.choose_figure()
                    self.ready = False
                    return
                self.current = None
                self.current_player = (self.current_player + 1) % 2

            elif cage.color != "green" and cage.figure is not None and cage.figure.color == ["white", "black"][self.current_player]:
                self.current = (coordinate, cage)
                cage.figure.moves(coordinate, cage)
        string_cages = ""
        string_figures = ""
        for i in range(8):
            for j in range(8):
                string_cages += f"{self.dict_cages[(i, j)].color} "
                string_figures += f" {self.dict_cages[(i, j)].figure.color}_{self.dict_cages[(i, j)].figure.name}"
        return f"{string_cages},{string_figures}"



    # def choose_figure(self):
    #     self.ready = False
    #     color = ["white", "black"][self.current_player]
    #     button_queen = tk.Button(command=self.choose_queen, image = self.images[f"{color}_queen"], width=85, height=85, bg = "#FFFF99")
    #     button_horse = tk.Button(command=self.choose_horse, image= self.images[f"{color}_horse"], width=85, height=85, bg = "#FFFF99")
    #     button_elephant = tk.Button(command=self.choose_elephant, image= self.images[f"{color}_elephant"], width=85, height=85, bg = "#FFFF99")
    #     button_rook = tk.Button(command=self.choose_rook, image= self.images[f"{color}_rook"], width=85, height=85, bg = "#FFFF99")
    #     self.figure_buttons = [button_queen, button_horse, button_elephant, button_rook]
    #     button_rook.place(anchor="nw", x = self.coordinate[0] * self.square_size + 598, y = self.coordinate[1] * self.square_size + 80)
    #     button_elephant.place(anchor="nw", x = self.coordinate[0] * self.square_size + 598, y = self.coordinate[1] * self.square_size - 10)
    #     button_horse.place(anchor="nw", x = self.coordinate[0] * self.square_size + 598, y = self.coordinate[1] * self.square_size - 100)
    #     button_queen.place(anchor="nw", x = self.coordinate[0] * self.square_size + 598, y = self.coordinate[1] * self.square_size - 190)
    #
    # def choose_queen(self):
    #     self.ready = True
    #     color = ["white", "black"][self.current_player]
    #     self.canvas.move(self.dict_cages[self.coordinate].figure.image, 10000, 10000)
    #     self.dict_cages[self.coordinate] = Cage(color, self.coordinate, Queen(color, self.move_figures, self, self.coordinate))
    #     self.delete_buttons(color)
    #
    # def choose_horse(self):
    #     self.ready = True
    #     color = ["white", "black"][self.current_player]
    #     self.canvas.move(self.dict_cages[self.coordinate].figure.image, 10000, 10000)
    #     self.dict_cages[self.coordinate] = Cage(color, self.coordinate, Horse(color, self.move_figures, self, self.coordinate))
    #     self.delete_buttons(color)
    #
    # def choose_elephant(self):
    #     self.ready = True
    #     color = ["white", "black"][self.current_player]
    #     self.canvas.move(self.dict_cages[self.coordinate].figure.image, 10000, 10000)
    #     self.dict_cages[self.coordinate] = Cage(color, self.coordinate, Elephant(color, self.move_figures, self, self.coordinate))
    #     self.delete_buttons(color)
    #
    # def choose_rook(self):
    #     self.ready = True
    #     color = ["white", "black"][self.current_player]
    #     self.canvas.move(self.dict_cages[self.coordinate].figure.image, 10000, 10000)
    #     self.dict_cages[self.coordinate] = Cage(color, self.coordinate, Rook(color, self.move_figures, self, self.coordinate))
    #     self.delete_buttons(color)
    #
    # def delete_buttons(self, color):
    #     for button in self.figure_buttons:
    #         button.destroy()
    #     self.figure_buttons = []
    #     if color == "black":
    #         for i in range(len(self.black_player.figures)):
    #             if self.black_player.figures[i].coordinate == self.coordinate:
    #                 self.black_player.figures.pop(i)
    #                 break
    #         self.black_player.add_figure(self.dict_cages[self.coordinate].figure)
    #     else:
    #         for i in range(len(self.white_player.figures)):
    #             if self.white_player.figures[i].coordinate == self.coordinate:
    #                 self.white_player.figures.pop(i)
    #                 break
    #         self.white_player.add_figure(self.dict_cages[self.coordinate].figure)
    #     self.current = None
    #     self.current_player = (self.current_player + 1) % 2
        
