class Rook:
    def __init__(self, color, move_figures, game):
        self.move_figures = move_figures
        self.game = game
        self.name = "rook"
        self.color = color

    def moves(self, coordinate, cage):
        self.move_figures.draw([x for x in self.get_moves(coordinate, cage) if x in
                   self.move_figures.get_possible_defense_moves(cage.figure.color, self)])

    def get_moves(self, coordinate, cage):
        x, y = coordinate
        color = cage.figure.color
        possible_moves = []

        # Проверяем возможные ходы вверх
        for dy in range(1, 8):
            if y - dy < 0:
                break
            target_cage = self.game.dict_cages[(x, y - dy)]
            if target_cage.figure is None:
                possible_moves.append((x, y - dy))
            else:
                if target_cage.figure.color != color:
                    possible_moves.append((x, y - dy))
                break

        # Проверяем возможные ходы вниз
        for dy in range(1, 8):
            if y + dy >= 8:
                break
            target_cage = self.game.dict_cages[(x, y + dy)]
            if target_cage.figure is None:

                possible_moves.append((x, y + dy))
            else:
                if target_cage.figure.color != color:
                    possible_moves.append((x, y + dy))
                break

        # Проверяем возможные ходы влево
        for dx in range(1, 8):
            if x - dx < 0:
                break
            target_cage = self.game.dict_cages[(x - dx, y)]
            if target_cage.figure is None:
                possible_moves.append((x - dx, y))
            else:
                if target_cage.figure.color != color:
                    possible_moves.append((x - dx, y))
                break

        # Проверяем возможные ходы вправо
        for dx in range(1, 8):
            if x + dx >= 8:
                break
            target_cage = self.game.dict_cages[(x + dx, y)]
            if target_cage.figure is None:
                possible_moves.append((x + dx, y))
            else:
                if target_cage.figure.color != color:
                    possible_moves.append((x + dx, y))
                break

        return possible_moves