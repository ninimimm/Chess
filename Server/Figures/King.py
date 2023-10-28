class King:
    def __init__(self, color, move_figures, game, coordinate, index):
        self.index = index
        self.coordinate = coordinate
        self.move_figures = move_figures
        self.game = game
        self.name = "king"
        self.color = color
        self.last_move = None

    def __str__(self): # pragma: no cover
        return f"{self.name[0]},{self.color[0]},{self.coordinate}"

    def moves(self, cage, dict_cages): # pragma: no cover
        self.move_figures.draw(self.get_possible_moves(cage, dict_cages))

    def get_possible_moves(self, cage, dict_cages): # pragma: no cover
        return list(self.move_figures.get_possible_defense_moves(cage.figure.color, dict_cages))

    def get_moves(self, coordinate, cage, dict_cages):
        x, y = coordinate
        color = cage.figure.color
        possible_moves = [(x + dx, y + dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if dx != 0 or dy != 0]
        possible = set()
        if self.last_move is None and all(dict_cages[(x, y)].figure is None for x in range(x-1, 0, -1))\
                and dict_cages[(0, y)].figure is not None and dict_cages[(0, 0)].figure.name == "rook"\
                and dict_cages[(0, y)].figure.last_move is None:
            possible.add((1, y))
        if self.last_move is None and all(dict_cages[(x, y)].figure is None for x in range(x+1, 7)) \
                and dict_cages[(7, y)].figure is not None and dict_cages[(7, 0)].figure.name == "rook" \
                and dict_cages[(7, y)].figure.last_move is None:
            possible.add((5, y))
        for move in possible_moves:
            if 0 <= move[0] < 8 and 0 <= move[1] < 8:
                target_cage = dict_cages[move]
                if target_cage.figure is None or target_cage.figure.color != color:
                    possible.add(move)
        return possible