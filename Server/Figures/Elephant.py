class Elephant:
    def __init__(self, color, move_figures, game, coordinate, index):
        self.index = index
        self.coordinate = coordinate
        self.move_figures = move_figures
        self.game = game
        self.name = "elephant"
        self.color = color
        if color == "white":
            game.index_white_elephant += 1
        else:
            game.index_black_elephant += 1

    def __str__(self): # pragma: no cover
        return f"{self.name[0]},{self.color[0]},{self.coordinate}"

    def moves(self, coordinate, cage, dict_cages): # pragma: no cover
        self.move_figures.draw(self.get_possible_moves(coordinate, cage, dict_cages))

    def get_possible_moves(self, coordinate, cage, dict_cages):
        possible_moves = self.move_figures.get_possible_defense_moves(cage.figure.color, dict_cages)
        return [x for x in self.get_moves(coordinate, cage, dict_cages) if x in possible_moves]

    def get_moves(self, coordinate, cage, dict_cages):
        x, y = coordinate
        color = cage.figure.color
        directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
        possible_moves = set()

        for dx, dy in directions:
            for i in range(1, 8):
                new_x, new_y = x + i * dx, y + i * dy
                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    target_cage = dict_cages[(new_x, new_y)]
                    if target_cage.figure is None:
                        possible_moves.add((new_x, new_y))
                    elif target_cage.figure.color != color:
                        possible_moves.add((new_x, new_y))
                        break
                    else:
                        break
                else:
                    break
        return possible_moves