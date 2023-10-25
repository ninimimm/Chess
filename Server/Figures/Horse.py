class Horse:
    def __init__(self, color, move_figures, game, coordinate, index):
        self.index = index
        self.coordinate = coordinate
        self.move_figures = move_figures
        self.game = game
        self.name = "horse"
        self.color = color
        if color == "white":
            self.game.index_white_horse += 1
        else:
            self.game.index_black_horse += 1

    def __str__(self): # pragma: no cover
        return f"{self.name[0]},{self.color[0]},{self.coordinate}"

    def moves(self, cage, dict_cages): # pragma: no cover
        self.move_figures.draw(self.get_possible_moves(coordinate, cage, dict_cages))

    def get_possible_moves(self, cage, dict_cages): # pragma: no cover
        return list(self.move_figures.get_possible_defense_moves(cage.figure.color, dict_cages))

    def get_moves(self, coordinate, cage, dict_cages):
        x, y = coordinate
        color = cage.figure.color
        possible_moves = [
            (x + 2, y + 1), (x + 2, y - 1),
            (x - 2, y + 1), (x - 2, y - 1),
            (x + 1, y + 2), (x + 1, y - 2),
            (x - 1, y + 2), (x - 1, y - 2)
        ]
        possible = set()
        for move in possible_moves:
            if 0 <= move[0] < 8 and 0 <= move[1] < 8:
                target_cage = dict_cages[move]
                if target_cage.figure is None or target_cage.figure.color != color:
                    possible.add(move)

        return possible