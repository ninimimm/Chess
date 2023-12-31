class Rook:
    def __init__(self, color, move_figures, game, coordinate, index):
        self.index = index
        self.move_figures = move_figures
        self.game = game
        self.name = "rook"
        self.color = color
        self.coordinate = coordinate
        self.last_move = None
        if color == "white":
            self.game.index_white_rook += 1
        else:
            self.game.index_black_rook += 1

    def __str__(self): # pragma: no cover
        return f"{self.name[0]},{self.color[0]},{self.coordinate}"

    def moves(self, cage, dict_cages): # pragma: no cover
        self.move_figures.draw(self.get_possible_moves(cage, dict_cages))

    def get_possible_moves(self, cage, dict_cages): # pragma: no cover
        return list(self.move_figures.get_possible_defense_moves(cage.figure.color, dict_cages))

    def get_moves(self, coordinate, cage, dict_cages):
        x, y = coordinate
        color = cage.figure.color
        possible_moves = set()

        # Проверяем возможные ходы вверх
        for dy in range(1, 8):
            if y - dy < 0:
                break
            target_cage = dict_cages[(x, y - dy)]
            if target_cage.figure is None:
                possible_moves.add((x, y - dy))
            else:
                if target_cage.figure.color != color:
                    possible_moves.add((x, y - dy))
                break

        # Проверяем возможные ходы вниз
        for dy in range(1, 8):
            if y + dy >= 8:
                break
            target_cage = dict_cages[(x, y + dy)]
            if target_cage.figure is None:

                possible_moves.add((x, y + dy))
            else:
                if target_cage.figure.color != color:
                    possible_moves.add((x, y + dy))
                break

        # Проверяем возможные ходы влево
        for dx in range(1, 8):
            if x - dx < 0:
                break
            target_cage = dict_cages[(x - dx, y)]
            if target_cage.figure is None:
                possible_moves.add((x - dx, y))
            else:
                if target_cage.figure.color != color:
                    possible_moves.add((x - dx, y))
                break

        # Проверяем возможные ходы вправо
        for dx in range(1, 8):
            if x + dx >= 8:
                break
            target_cage = dict_cages[(x + dx, y)]
            if target_cage.figure is None:
                possible_moves.add((x + dx, y))
            else:
                if target_cage.figure.color != color:
                    possible_moves.add((x + dx, y))
                break

        return possible_moves