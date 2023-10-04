import tkinter as tk
from Game import Game
from PIL import Image, ImageTk  # Импортируем Image и ImageTk из библиотеки Pillow

class Gui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Шахматная доска")
        self.root.attributes('-fullscreen', True)
        self.canvas = tk.Canvas(self.root, width=1000, height=800)
        self.canvas.pack()

        self.square_size = 90
        self.diffy = 80
        self.diffx = 140

        self.load_images()
        self.game = Game(self.root, self.images, self.canvas, self.square_size, self.diffy, self.diffx)

    def load_images(self):
        self.images = {}
        for piece in ["pawn", "rook", "horse", "elephant", "queen", "king"]:
            for color in ["white", "black"]:
                filename = rf"output\{color}_{piece}.png"
                image = Image.open(filename)
                image = image.resize((int(image.width), int(image.height)), Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(image)
                self.images[f"{color}_{piece}"] = photo