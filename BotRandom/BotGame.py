import tkinter as tk
import random
import functools
import threading

class BotGame:
    def __init__(self, shared_data):
        self.shared_data = shared_data
        self.color = None
        self.send_color = None
        self.prev_cord = None
        self.evals = {}
        self.values = {
            "pawn": 10,
            "horse": 30,
            "elephant": 30,
            "rook": 50,
            "queen": 90,
            "king": 900}
        self.update_eval()
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
        self.figure_buttons = []
        self.coordinate = None
        self.string_images = [["" for _ in range(8)] for _ in range(8)]
        for i in range(len(self.string_images)):
            for j in range(len(self.string_images)):
                if j < 2:
                    if j == 1:
                        self.string_images[i][j] = f"white_pawn{self.index_white_pawn}"
                        self.index_white_pawn += 1
                    else:
                        if i == 0 or i == 7:
                            self.string_images[i][j] = f"white_rook{self.index_white_rook}"
                            self.index_white_rook += 1

                        elif i == 1 or i == 6:
                            self.string_images[i][j] = f"white_horse{self.index_white_horse}"
                            self.index_white_horse += 1
                        elif i == 2 or i == 5:
                            self.string_images[i][j] = f"white_elephant{self.index_white_elephant}"
                            self.index_white_elephant += 1
                        elif i == 4:
                            self.string_images[i][j] = "white_queen0"
                            self.index_white_queen += 1
                        else:
                            self.string_images[i][j] = "white_king0"
                elif j > 5:
                    if j == 6:
                        self.string_images[i][j] = f"black_pawn{self.index_black_pawn}"
                        self.index_black_pawn += 1
                    else:
                        if i == 0 or i == 7:
                            self.string_images[i][j] = f"black_rook{self.index_black_rook}"
                            self.index_black_rook += 1
                        elif i == 1 or i == 6:
                            self.string_images[i][j] = f"black_horse{self.index_black_horse}"
                            self.index_black_horse += 1
                        elif i == 2 or i == 5:
                            self.string_images[i][j] = f"black_elephant{self.index_black_elephant}"
                            self.index_black_elephant += 1
                        elif i == 4:
                            self.string_images[i][j] = "black_queen0"
                            self.index_black_queen += 1
                        else:
                            self.string_images[i][j] = "black_king0"
        self.shared_data.game = self
        self.shared_data.copy_field = self.string_images.copy()

    def trackcalls(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if not hasattr(wrapper, "lock"):
                wrapper.lock = threading.Lock()

            with wrapper.lock:
                if hasattr(wrapper, "is_running") and wrapper.is_running:
                    return True
                wrapper.is_running = True

            try:
                result = func(*args, **kwargs)
            finally:
                with wrapper.lock:
                    wrapper.is_running = False

            return result

        def is_running():
            with wrapper.lock:
                return wrapper.is_running

        wrapper.is_running = False
        wrapper.is_running = is_running

        return wrapper

    @trackcalls
    def get_content(self, dict, color):
        if self.color is None:
            self.color = color
        print(self.send_color)
        enemy_color = "black" if color == "black" else "white"
        max_weight = -9999
        variants = []
        print(dict)
        for key in dict:
            print("мотивация!")
            for coordinate in dict[key]:
                weight = 0
                eval_coord = coordinate if color == "white" else (coordinate[1], coordinate[0])
                if enemy_color in self.shared_data.copy_field[coordinate[0]][coordinate[1]]:
                    print(self.shared_data.copy_field[coordinate[0]][coordinate[1]])
                    weight += self.values[self.shared_data.copy_field[coordinate[0]][coordinate[1]].split("_")[1][:-1]]
                weight += self.evals[self.shared_data.copy_field[key[0]][key[1]].split("_")[1][:-1]][eval_coord[0]][eval_coord[1]]
                if weight > max_weight:
                    max_weight = weight
                    variants = [[key, coordinate]]
                    print(variants)
                elif weight == max_weight:
                    variants.append([key, coordinate])
        return variants[random.randint(0, len(variants) - 1)]
    def update_eval(self):
        self.evals["pawn"] = [
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0],
            [1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0],
            [0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5],
            [0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0],
            [0.5, -0.5, -1.0, 0.0, 0.0, -1.0, -0.5, 0.5],
            [0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
        self.evals["elephant"] = [
            [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
            [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0],
            [-1.0, 0.0, 0.5, 1.0, 1.0, 0.5, 0.0, -1.0],
            [-1.0, 0.5, 0.5, 1.0, 1.0, 0.5, 0.5, -1.0],
            [-1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.0],
            [-1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0],
            [-1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, -1.0],
            [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]]
        self.evals["horse"] = [
            [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
            [-4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0],
            [-3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0],
            [-3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0],
            [-3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0],
            [-3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0],
            [-4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0],
            [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]]
        self.evals["rook"] = [
            [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
            [0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5],
            [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
            [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
            [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
            [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
            [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
            [0.0,   0.0, 0.0,  0.5,  0.5,  0.0,  0.0,  0.0]]
        self.evals["king"] = [
            [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
            [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
            [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
            [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
            [-2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
            [-1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
            [2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0],
            [2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0]]
        self.evals["queen"] = [
            [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
            [-1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
            [-1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
            [-0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
            [0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
            [-1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
            [-1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0],
            [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]]