class King:
    def __init__(self, color, move_figures, game):
        self.move_figures = move_figures
        self.game = game
        self.name = "king"
        self.color = color

    def moves(self, coordinate, cage):
        self.move_figures.draw([x for x in self.get_moves(coordinate, cage) if x in
                   self.move_figures.get_possible_defense_moves(cage.figure.color, self)])

    def get_moves(self, coordinate, cage):
        x, y = coordinate
        color = cage.figure.color
        possible_moves = [(x + dx, y + dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if dx != 0 or dy != 0]
        possible = []

        for move in possible_moves:
            if 0 <= move[0] < 8 and 0 <= move[1] < 8:
                target_cage = self.game.dict_cages[move]
                if target_cage.figure is None or target_cage.figure.color != color:
                    possible.append(move)
        return possible