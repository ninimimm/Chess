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
import Clientmain


class ClientGame:
    def __init__(self, root, images, canvas, square_size, diffy, diffx):
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
                        self.string_images[i][j] = "white_pawn"
                        self.dict_images["white_pawn"] = self.canvas.create_image(i * self.square_size + self.diffx - 2,
                                                 j * self.square_size + self.diffy - 20,
                                                 anchor=tk.NW, image=images["white_pawn"])

                    else:
                        if i == 0 or i == 7:
                            self.string_images[i][j] = "white_rook"
                            self.dict_images["white_rook"] = self.canvas.create_image(i * self.square_size + self.diffx - 2,
                                                     j * self.square_size + self.diffy - 20,
                                                     anchor=tk.NW, image=images["white_rook"])

                        elif i == 1 or i == 6:
                            self.string_images[i][j] = "white_horse"
                            self.dict_images["white_horse"] = self.canvas.create_image(i * self.square_size + self.diffx - 2,
                                                     j * self.square_size + self.diffy - 20,
                                                     anchor=tk.NW, image=images["white_horse"])
                        elif i == 2 or i == 5:
                            self.string_images[i][j] = "white_elephant"
                            self.dict_images["white_elephant"] = self.canvas.create_image(i * self.square_size + self.diffx - 2,
                                                     j * self.square_size + self.diffy - 20,
                                                     anchor=tk.NW, image=images["white_elephant"])
                        elif i == 3:
                            self.string_images[i][j] = "white_queen"
                            self.dict_images["white_queen"] = self.canvas.create_image(i * self.square_size + self.diffx - 2,
                                                     j * self.square_size + self.diffy - 20,
                                                     anchor=tk.NW, image=images["white_queen"])
                        else:
                            self.string_images[i][j] = "white_king"
                            self.dict_images["white_king"] = self.canvas.create_image(i * self.square_size + self.diffx - 2,
                                                     j * self.square_size + self.diffy - 20,
                                                     anchor=tk.NW, image=images["white_king"])
                elif j > 5:
                    if j == 6:
                        self.string_images[i][j] = "black_pawn"
                        self.dict_images["black_pawn"] = self.canvas.create_image(i * self.square_size + self.diffx - 2,
                                                 j * self.square_size + self.diffy - 20,
                                                 anchor=tk.NW, image=images["black_pawn"])
                    else:
                        if i == 0 or i == 7:
                            self.string_images[i][j] = "black_rook"
                            self.dict_images["black_rook"] = self.canvas.create_image(i * self.square_size + self.diffx - 2,
                                                     j * self.square_size + self.diffy - 20,
                                                     anchor=tk.NW, image=images["black_rook"])
                        elif i == 1 or i == 6:
                            self.string_images[i][j] = "black_horse"
                            self.dict_images["black_horse"] = self.canvas.create_image(i * self.square_size + self.diffx - 2,
                                                     j * self.square_size + self.diffy - 20,
                                                     anchor=tk.NW, image=images["black_horse"])
                        elif i == 2 or i == 5:
                            self.string_images[i][j] = "black_elephant"
                            self.dict_images["black_elephant"] = self.canvas.create_image(i * self.square_size + self.diffx - 2,
                                                     j * self.square_size + self.diffy - 20,
                                                     anchor=tk.NW, image=images["black_elephant"])
                        elif i == 3:
                            self.string_images[i][j] = "black_queen"
                            self.dict_images["black_queen"] = self.canvas.create_image(i * self.square_size + self.diffx - 2,
                                                     j * self.square_size + self.diffy - 20,
                                                     anchor=tk.NW, image=images["black_queen"])
                        else:
                            self.string_images[i][j] = "black_king"
                            self.dict_images["black_king"] = self.canvas.create_image(i * self.square_size + self.diffx - 2,
                                                     j * self.square_size + self.diffy - 20,
                                                     anchor=tk.NW, image=images["black_king"])


    def on_click(self, event):
        self.coordinate = ((event.x - self.diffx) // self.square_size, (event.y - self.diffy) // self.square_size)
        Clientmain.connection(self.coordinate, self, self.client)

    def get_content(self, cages, figures):
        for i in range(8):
            for j in range(8):
                self.canvas.itemconfig(self.squares[i][j], fill=cages[i * 8 + j])
                if figures[i * 8 + j] != "None":
                    self.string_images[j][i] = figures[i * 8 + j]
                else:
                    self.string_images[j][i] = ""
                self.canvas.move(self.dict_images[figures[i * 8 + j]], j * self.square_size + self.diffx - 2, i * self.square_size + self.diffy - 20)

