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
from PIL import Image, ImageTk


class ClientGame:
    def __init__(self, root, images, canvas, square_size, diffy, diffx, shared_data):
        self.shared_data = shared_data
        self.color = None
        self.prev_cord = None
        self.index_white_pawn = 0
        self.index_black_pawn = 0
        self.index_white_rook = 0
        self.index_black_rook = 0
        self.index_white_horse = 0
        self.index_black_horse = 0
        self.index_white_elephant = 0
        self.index_black_elephant = 0
        self.client = None
        self.root = root
        self.canvas = canvas
        self.images = images
        self.dict_images = {}
        self.square_size = square_size
        self.diffy = diffy
        self.diffx = diffx
        self.canvas.bind('<Button-1>', self.on_click)
        self.figure_buttons = []
        self.coordinate = None
        self.squares = [[self.canvas.create_rectangle(i * self.square_size + self.diffx,
                                                      j * self.square_size + self.diffy,
                                                      i * self.square_size + self.square_size + self.diffx,
                                                      j * self.square_size + self.square_size + self.diffy,
                                                      fill=["white", "black"][(i + j) % 2]) for i in range(8)] for j in range(8)]
        self.string_images = [["" for _ in range(8)] for _ in range(8)]
        for i in range(len(self.string_images)):
            for j in range(len(self.string_images)):
                if j < 2:
                    if j == 1:
                        self.string_images[i][j] = f"white_pawn{self.index_white_pawn}"
                        self.dict_images[f"white_pawn{self.index_white_pawn}"] = [self.canvas.create_image(i * self.square_size + self.diffx - 2,
                                                 j * self.square_size + self.diffy - 20,
                                                 anchor=tk.NW, image=images["white_pawn"]), (j, i)]
                        self.index_white_pawn += 1
                    else:
                        if i == 0 or i == 7:
                            self.string_images[i][j] = f"white_rook{self.index_white_rook}"
                            self.dict_images[f"white_rook{self.index_white_rook}"] = [self.canvas.create_image(i * self.square_size + self.diffx - 2,
                                                     j * self.square_size + self.diffy - 20,
                                                     anchor=tk.NW, image=images["white_rook"]), (j, i)]
                            self.index_white_rook += 1

                        elif i == 1 or i == 6:
                            self.string_images[i][j] = f"white_horse{self.index_white_horse}"
                            self.dict_images[f"white_horse{self.index_white_horse}"] = [self.canvas.create_image(i * self.square_size + self.diffx - 2,
                                                     j * self.square_size + self.diffy - 20,
                                                     anchor=tk.NW, image=images["white_horse"]), (j, i)]
                            self.index_white_horse += 1
                        elif i == 2 or i == 5:
                            self.string_images[i][j] = f"white_elephant{self.index_white_elephant}"
                            self.dict_images[f"white_elephant{self.index_white_elephant}"] = [self.canvas.create_image(i * self.square_size + self.diffx - 2,
                                                     j * self.square_size + self.diffy - 20,
                                                     anchor=tk.NW, image=images["white_elephant"]), (j, i)]
                            self.index_white_elephant += 1
                        elif i == 3:
                            self.string_images[i][j] = "white_queen0"
                            self.dict_images["white_queen0"] = [self.canvas.create_image(i * self.square_size + self.diffx - 2,
                                                     j * self.square_size + self.diffy - 20,
                                                     anchor=tk.NW, image=images["white_queen"]), (j, i)]
                        else:
                            self.string_images[i][j] = "white_king0"
                            self.dict_images["white_king0"] = [self.canvas.create_image(i * self.square_size + self.diffx - 2,
                                                     j * self.square_size + self.diffy - 20,
                                                     anchor=tk.NW, image=images["white_king"]), (j, i)]
                elif j > 5:
                    if j == 6:
                        self.string_images[i][j] = f"black_pawn{self.index_black_pawn}"
                        self.dict_images[f"black_pawn{self.index_black_pawn}"] = [self.canvas.create_image(i * self.square_size + self.diffx - 2,
                                                 j * self.square_size + self.diffy - 20,
                                                 anchor=tk.NW, image=images["black_pawn"]), (j, i)]
                        self.index_black_pawn += 1
                    else:
                        if i == 0 or i == 7:
                            self.string_images[i][j] = f"black_rook{self.index_black_rook}"
                            self.dict_images[f"black_rook{self.index_black_rook}"] = [self.canvas.create_image(i * self.square_size + self.diffx - 2,
                                                     j * self.square_size + self.diffy - 20,
                                                     anchor=tk.NW, image=images["black_rook"]), (j, i)]
                            self.index_black_rook += 1
                        elif i == 1 or i == 6:
                            self.string_images[i][j] = f"black_horse{self.index_black_horse}"
                            self.dict_images[f"black_horse{self.index_black_horse}"] = [self.canvas.create_image(i * self.square_size + self.diffx - 2,
                                                     j * self.square_size + self.diffy - 20,
                                                     anchor=tk.NW, image=images["black_horse"]), (j, i)]
                            self.index_black_horse += 1
                        elif i == 2 or i == 5:
                            self.string_images[i][j] = f"black_elephant{self.index_black_elephant}"
                            self.dict_images[f"black_elephant{self.index_black_elephant}"] = [self.canvas.create_image(i * self.square_size + self.diffx - 2,
                                                     j * self.square_size + self.diffy - 20,
                                                     anchor=tk.NW, image=images["black_elephant"]), (j, i)]
                            self.index_black_elephant += 1
                        elif i == 3:
                            self.string_images[i][j] = "black_queen0"
                            self.dict_images["black_queen0"] = [self.canvas.create_image(i * self.square_size + self.diffx - 2,
                                                     j * self.square_size + self.diffy - 20,
                                                     anchor=tk.NW, image=images["black_queen"]), (j, i)]
                        else:
                            self.string_images[i][j] = "black_king0"
                            self.dict_images["black_king0"] = [self.canvas.create_image(i * self.square_size + self.diffx - 2,
                                                     j * self.square_size + self.diffy - 20,
                                                     anchor=tk.NW, image=images["black_king"]), (j, i)]
        self.shared_data.game = self

    def on_click(self, event):
        cord = ((event.x - self.diffx) // self.square_size, (event.y - self.diffy) // self.square_size)
        if self.color is None or self.string_images[cord[0]][cord[1]].split('_')[0] == self.color:
            self.prev_cord = cord
        self.coordinate = cord
        self.shared_data.coordinate = self.coordinate

    def get_content(self, cages, figures, color):
        self.color = color
        for i in range(8):
            for j in range(8):
                self.canvas.itemconfig(self.squares[i][j], fill=cages[i * 8 + j])
                if figures[i * 8 + j] != "None":
                    self.string_images[j][i] = figures[i * 8 + j]
                    self.canvas.move(self.dict_images[figures[i * 8 + j]][0],
                                     (j - self.dict_images[figures[i * 8 + j]][1][1]) * self.square_size,
                                     (i - self.dict_images[figures[i * 8 + j]][1][0]) * self.square_size)
                    self.dict_images[figures[i * 8 + j]][1] = (i, j)
                else:
                    self.string_images[j][i] = ""
