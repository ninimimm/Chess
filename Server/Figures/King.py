class King:
    def __init__(self, color, move_figures, game, coordinate, index):
        self.index = index
        self.coordinate = coordinate
        self.move_figures = move_figures
        self.game = game
        self.name = "king"
        self.color = color

    def __str__(self):
        return f"{self.name[0]},{self.color[0]},{self.coordinate}"

    def moves(self, coordinate, cage, dict_cages):
        self.move_figures.draw(self.get_possible_moves(coordinate, cage, dict_cages))

    def get_possible_moves(self, coordinate, cage, dict_cages):
        possible_moves = self.move_figures.get_possible_defense_moves(cage.figure.color, dict_cages)
        return [x for x in self.get_moves(coordinate, cage, dict_cages) if x in possible_moves]

    def get_moves(self, coordinate, cage, dict_cages):
        x, y = coordinate
        color = cage.figure.color
        possible_moves = [(x + dx, y + dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if dx != 0 or dy != 0]
        possible = []
        for move in possible_moves:
            if 0 <= move[0] < 8 and 0 <= move[1] < 8:
                target_cage = dict_cages[move]
                if target_cage.figure is None or target_cage.figure.color != color:
                    possible.append(move)
        return possible