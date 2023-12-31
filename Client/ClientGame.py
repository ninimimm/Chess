import tkinter as tk


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
        self.index_white_queen = 0
        self.index_black_queen = 0
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
                        elif i == 4:
                            self.string_images[i][j] = "white_queen0"
                            self.dict_images["white_queen0"] = [self.canvas.create_image(i * self.square_size + self.diffx - 2,
                                                     j * self.square_size + self.diffy - 20,
                                                     anchor=tk.NW, image=images["white_queen"]), (j, i)]
                            self.index_white_queen += 1
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
                        elif i == 4:
                            self.string_images[i][j] = "black_queen0"
                            self.dict_images["black_queen0"] = [self.canvas.create_image(i * self.square_size + self.diffx - 2,
                                                     j * self.square_size + self.diffy - 20,
                                                     anchor=tk.NW, image=images["black_queen"]), (j, i)]
                            self.index_black_queen += 1
                        else:
                            self.string_images[i][j] = "black_king0"
                            self.dict_images["black_king0"] = [self.canvas.create_image(i * self.square_size + self.diffx - 2,
                                                     j * self.square_size + self.diffy - 20,
                                                     anchor=tk.NW, image=images["black_king"]), (j, i)]
        self.shared_data.game = self
        self.our_text = self.canvas.create_text(910, 400, text=f"Вы:\n{self.color}", fill="black", font=("Helvetica", 16))
        self.enemy_text = self.canvas.create_text(939, 450, text=f"Противник:\n{self.color}", fill="black", font=("Helvetica", 16))
    def on_click(self, event):
        cord = ((event.x - self.diffx) // self.square_size, (event.y - self.diffy) // self.square_size)
        if self.color is None or self.string_images[cord[0]][cord[1]].split('_')[0] == self.color:
            self.prev_cord = cord
        self.coordinate = cord
        self.shared_data.coordinate = self.coordinate

    def get_content(self, cages, figures, color):
        if self.color is None:
            self.color = color
        if "None" in self.canvas.itemcget(self.our_text, 'text'):
            self.canvas.itemconfig(self.our_text, text=f"Вы:\n{color}")
            self.canvas.itemconfig(self.enemy_text, text=f"Противник:\n{'black' if color == 'white' else 'white'}")
        for i in range(8):
            for j in range(8):
                if self.string_images[i][j] != '' and self.string_images[i][j] not in figures:
                    self.canvas.move(self.dict_images[self.string_images[i][j]][0], 10000, 10000)
        for i in range(8):
            for j in range(8):
                if cages != "None":
                    self.canvas.itemconfig(self.squares[i][j], fill=cages[i * 8 + j])
                if figures[i * 8 + j] != "None":
                    self.string_images[j][i] = figures[i * 8 + j]
                    if figures[i * 8 + j] not in self.dict_images:
                        self.string_images[i][j] = figures[i * 8 + j]
                        self.dict_images[figures[i * 8 + j]] = [
                            self.canvas.create_image(i * self.square_size + self.diffx - 2,
                                                     j * self.square_size + self.diffy - 20,
                                                     anchor=tk.NW, image=self.images[figures[i * 8 + j][:-1]]), (j, i)]
                    self.canvas.move(self.dict_images[figures[i * 8 + j]][0],
                                     (j - self.dict_images[figures[i * 8 + j]][1][1]) * self.square_size,
                                     (i - self.dict_images[figures[i * 8 + j]][1][0]) * self.square_size)
                    self.dict_images[figures[i * 8 + j]][1] = (i, j)
                else:
                    self.string_images[j][i] = ""

    def choose_figure(self, color):
        button_queen = tk.Button(command=lambda: self.choose_queen(color), image = self.images[f"{color}_queen"], width=85, height=85, bg = "#FFFF99")
        button_horse = tk.Button(command=lambda: self.choose_horse(color), image= self.images[f"{color}_horse"], width=85, height=85, bg = "#FFFF99")
        button_elephant = tk.Button(command=lambda: self.choose_elephant(color), image= self.images[f"{color}_elephant"], width=85, height=85, bg = "#FFFF99")
        button_rook = tk.Button(command=lambda: self.choose_rook(color), image= self.images[f"{color}_rook"], width=85, height=85, bg = "#FFFF99")
        self.figure_buttons = [button_queen, button_horse, button_elephant, button_rook]
        button_rook.place(anchor="nw", x = self.coordinate[0] * self.square_size + 598, y = self.coordinate[1] * self.square_size + 80)
        button_elephant.place(anchor="nw", x = self.coordinate[0] * self.square_size + 598, y = self.coordinate[1] * self.square_size - 10)
        button_horse.place(anchor="nw", x = self.coordinate[0] * self.square_size + 598, y = self.coordinate[1] * self.square_size - 100)
        button_queen.place(anchor="nw", x = self.coordinate[0] * self.square_size + 598, y = self.coordinate[1] * self.square_size - 190)
        self.canvas.move(self.dict_images[self.string_images[self.coordinate[0]][self.coordinate[1]]][0], 10000, 10000)
        self.canvas.move(self.dict_images[self.string_images[self.prev_cord[0]][self.prev_cord[1]]][0], 10000, 10000)

    def choose_queen(self, color):
        self.delete_buttons(color)
        self.shared_data.answer_button = f"Queen,{self.coordinate[0]} {self.coordinate[1]}"
        self.dict_images[f"{color}_queen{self.index_white_queen}"] = [
            self.canvas.create_image(self.coordinate[0] * self.square_size + self.diffx - 2,
                                     self.coordinate[1] * self.square_size + self.diffy - 20,
                                     anchor=tk.NW, image=self.images[f"{color}_queen"]), (self.coordinate[1], self.coordinate[0])]

    def choose_horse(self, color):
        self.delete_buttons(color)
        self.shared_data.answer_button = f"Horse,{self.coordinate[0]} {self.coordinate[1]}"
        self.dict_images[f"{color}_horse{self.index_white_horse}"] = [
            self.canvas.create_image(self.coordinate[0] * self.square_size + self.diffx - 2,
                                     self.coordinate[1] * self.square_size + self.diffy - 20,
                                     anchor=tk.NW, image=self.images[f"{color}_horse"]),
            (self.coordinate[1], self.coordinate[0])]

    def choose_elephant(self, color):
        self.delete_buttons(color)
        self.shared_data.answer_button = f"Elephant,{self.coordinate[0]} {self.coordinate[1]}"
        self.dict_images[f"{color}_elephant{self.index_white_elephant}"] = [
            self.canvas.create_image(self.coordinate[0] * self.square_size + self.diffx - 2,
                                     self.coordinate[1] * self.square_size + self.diffy - 20,
                                     anchor=tk.NW, image=self.images[f"{color}_elephant"]),
            (self.coordinate[1], self.coordinate[0])]

    def choose_rook(self, color):
        self.delete_buttons(color)
        self.shared_data.answer_button = f"Rook,{self.coordinate[0]} {self.coordinate[1]}"
        self.dict_images[f"{color}_rook{self.index_white_rook}"] = [
            self.canvas.create_image(self.coordinate[0] * self.square_size + self.diffx - 2,
                                     self.coordinate[1] * self.square_size + self.diffy - 20,
                                     anchor=tk.NW, image=self.images[f"{color}_rook"]),
            (self.coordinate[1], self.coordinate[0])]

    def delete_buttons(self, color):
        for button in self.figure_buttons:
            button.destroy()
        self.figure_buttons = []

