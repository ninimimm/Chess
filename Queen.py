class Queen:
    def __init__(self, color, move_figures, game, coordinate, index):
        self.index = index
        self.coordinate = coordinate
        self.move_figures = move_figures
        self.game = game
        self.name = "queen"
        self.color = color
        if color == "white":
            self.game.index_white_queen += 1
        else:
            self.game.index_black_queen += 1

    def __str__(self):
        return f"{self.name[0]},{self.color[0]},{self.coordinate}"

    def moves(self, coordinate, cage):
        possible_moves = self.move_figures.get_possible_defense_moves(cage.figure.color)
        self.move_figures.draw([x for x in self.get_moves(coordinate, cage) if x in possible_moves])

    def get_moves(self, coordinate, cage):
        x, y = coordinate
        color = cage.figure.color
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        possible = []
        for dx, dy in directions:
            for i in range(1, 8):
                new_x, new_y = x + i * dx, y + i * dy
                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    target_cage = self.game.dict_cages[(new_x, new_y)]
                    if target_cage.figure is None:
                        possible.append((new_x, new_y))
                    elif target_cage.figure.color != color:
                        possible.append((new_x, new_y))
                        break
                    else:
                        break
                else:
                    break
        return possible