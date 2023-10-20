import random
import copy

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
        self.is_running = False
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

    def get_content(self, dict, color):
        self.is_running = True
        if self.color is None:
            self.color = color
        # print(self.send_color)
        max_weight = -9999
        variants = {}
        find_variants = []
        # print(dict)
        copy_dict_1 = copy.deepcopy(self.shared_data.copy_field)
        for key in dict:
            # print("мотивация!")
            for coordinate in dict[key]:
                enemy_color = "white"
                first_weight = 0
                eval_coord = coordinate
                if enemy_color in self.shared_data.copy_field[coordinate[0]][coordinate[1]]:
                    # print(self.shared_data.copy_field[coordinate[0]][coordinate[1]])
                    first_weight += self.values[self.shared_data.copy_field[coordinate[0]][coordinate[1]].split("_")[1][:-1]]
                # print(key)
                # print(self.shared_data.copy_field[coordinate[0]][coordinate[1]])
                first_weight += self.evals[self.shared_data.copy_field[key[0]][key[1]].
                                           split("_")[1][:-1]][eval_coord[0]][eval_coord[1]]
                self.shared_data.copy_field[coordinate[0]][coordinate[1]] = self.shared_data.copy_field[key[0]][key[1]]
                self.shared_data.copy_field[key[0]][key[1]] = "None"
                self.send_color = "white"
                while not self.shared_data.can_use:
                    continue
                self.shared_data.can_use = False
                max_four_weight = -9999
                keys = []
                for enemy_key in self.shared_data.game_dict:
                    # print("мотивация!")
                    for enemy_coordinate in self.shared_data.game_dict[enemy_key]:
                        enemy_color = "black"
                        four_weight = 0
                        eval_coord = (enemy_coordinate[1], enemy_coordinate[0])
                        # print(eval_coord)
                        # print(enemy_key)
                        # print(self.shared_data.copy_field)
                        # print(self.shared_data.copy_field[enemy_key[0]][enemy_key[1]].split("_")[1])
                        if enemy_color in self.shared_data.copy_field[enemy_coordinate[0]][enemy_coordinate[1]]:
                            # print(self.shared_data.copy_field[enemy_coordinate[0]][enemy_coordinate[1]])
                            four_weight += self.values[self.shared_data.copy_field[enemy_coordinate[0]]
                                                       [enemy_coordinate[1]].split("_")[1][:-1]]
                        four_weight += self.evals[self.shared_data.copy_field[enemy_key[0]][enemy_key[1]].
                                                  split("_")[1][:-1]][eval_coord[0]][eval_coord[1]]
                        if four_weight > max_four_weight:
                            max_four_weight = four_weight
                            keys = [(enemy_key, enemy_coordinate)]
                        elif four_weight == max_four_weight:
                            keys.append((enemy_key, enemy_coordinate))
                if first_weight - max_four_weight in variants:
                    num = random.randint(0, len(keys) - 1)
                    variants[first_weight - max_four_weight].append([key, coordinate, keys[num][0], keys[num][1]])
                else:
                    num = random.randint(0, len(keys) - 1)
                    variants[first_weight - max_four_weight] = [[key, coordinate, keys[num][0], keys[num][1]]]
                self.shared_data.copy_field = copy.deepcopy(copy_dict_1)
        sorted_variants = sorted(variants.items(), reverse=True)
        best_variants = []
        count = 10
        while sorted_variants or count > 0:
            item = sorted_variants.pop()
            if len(item[1]) >= count:
                array = item[1]
                random.shuffle(array)
                for i in range(count):
                    best_variants.append((item[0], array[i]))
                count = 0
            else:
                for move in item[1]:
                    best_variants.append((item[0], move))
                    count -= 1
        print(variants)
        for i in range(10):
            print(f"рассматриваю {i} вариант")
            self.shared_data.copy_field = copy.deepcopy(copy_dict_1)
            self.shared_data.copy_field[best_variants[i][1][1][0]][best_variants[i][1][1][1]] = self.shared_data.copy_field[best_variants[i][1][0][0]][best_variants[i][1][0][1]]
            self.shared_data.copy_field[best_variants[i][1][0][0]][best_variants[i][1][0][1]] = "None"
            self.shared_data.copy_field[best_variants[i][1][3][0]][best_variants[i][1][3][1]] = self.shared_data.copy_field[best_variants[i][1][2][0]][best_variants[i][1][2][1]]
            self.shared_data.copy_field[best_variants[i][1][2][0]][best_variants[i][1][2][1]] = "None"
            self.send_color = "black"
            while not self.shared_data.can_use:
                continue
            self.shared_data.can_use = False
            use_dict = self.shared_data.game_dict
            copy_dict_2 = copy.deepcopy(self.shared_data.copy_field)
            for key in use_dict:
                print("ключ черный")
                # print("мотивация!")
                for coordinate in use_dict[key]:
                    print("коорд черный")
                    enemy_color = "white"
                    first_weight = 0
                    eval_coord = coordinate
                    if enemy_color in self.shared_data.copy_field[coordinate[0]][coordinate[1]]:
                        # print(self.shared_data.copy_field[coordinate[0]][coordinate[1]])
                        first_weight += self.values[
                            self.shared_data.copy_field[coordinate[0]][coordinate[1]].split("_")[1][:-1]]
                    # print(key)
                    # print(self.shared_data.copy_field[coordinate[0]][coordinate[1]])
                    first_weight += self.evals[self.shared_data.copy_field[key[0]][key[1]].
                                               split("_")[1][:-1]][eval_coord[0]][eval_coord[1]]
                    self.shared_data.copy_field[coordinate[0]][coordinate[1]] = self.shared_data.copy_field[key[0]][
                        key[1]]
                    self.shared_data.copy_field[key[0]][key[1]] = "None"
                    self.send_color = "white"
                    while not self.shared_data.can_use:
                        continue
                    self.shared_data.can_use = False
                    max_four_weight = -9999
                    for enemy_key in self.shared_data.game_dict:
                        print("ключ белый")
                        # print("мотивация!")
                        for enemy_coordinate in self.shared_data.game_dict[enemy_key]:
                            print("коорд белый")
                            enemy_color = "black"
                            four_weight = 0
                            eval_coord = (enemy_coordinate[1], enemy_coordinate[0])
                            # print(eval_coord)
                            # print(enemy_key)
                            # print(self.shared_data.copy_field)
                            # print(self.shared_data.copy_field[enemy_key[0]][enemy_key[1]].split("_")[1])
                            if enemy_color in self.shared_data.copy_field[enemy_coordinate[0]][enemy_coordinate[1]]:
                                # print(self.shared_data.copy_field[enemy_coordinate[0]][enemy_coordinate[1]])
                                four_weight += self.values[self.shared_data.copy_field[enemy_coordinate[0]]
                                                           [enemy_coordinate[1]].split("_")[1][:-1]]
                            four_weight += self.evals[self.shared_data.copy_field[enemy_key[0]][enemy_key[1]].
                                                      split("_")[1][:-1]][eval_coord[0]][eval_coord[1]]
                            max_four_weight = max(max_four_weight, four_weight)
                    if best_variants[i][0] + first_weight - max_four_weight > max_weight:
                        max_weight = best_variants[i][0] + first_weight - max_four_weight
                        find_variants = [[best_variants[i][1][0], best_variants[i][1][1]]]
                    elif best_variants[i][0] + first_weight - max_four_weight == max_weight:
                        find_variants.append([best_variants[i][1][0], best_variants[i][1][1]])
                    self.shared_data.copy_field = copy.deepcopy(copy_dict_2)
            self.shared_data.copy_field = copy.deepcopy(copy_dict_1)
        self.is_running = False
        print(find_variants)
        return find_variants[random.randint(0, len(find_variants) - 1)]
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