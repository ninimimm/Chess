class Pawn:
    def __init__(self, color, move_figures, game, coordinate, index):
        self.index = index
        self.coordinate = coordinate
        self.move_figures = move_figures
        self.game = game
        self.name = "pawn"
        self.color = color
        if color == "white":
            self.game.index_white_pawn += 1
        else:
            self.game.index_black_pawn += 1

    def __str__(self):
        return f"{self.name[0]},{self.color[0]},{self.coordinate}"

    def moves(self, coordinate, cage):
        possible_moves = self.move_figures.get_possible_defense_moves(cage.figure.color)
        self.move_figures.draw([x for x in self.get_moves(coordinate, cage) if x in possible_moves])

    def get_moves(self, coordinate, cage):
        x, y = coordinate
        color = cage.figure.color
        direction = 1 if color == "white" else -1  # Направление движения для белых и черных пешек
        possible_moves = []
        # Проверяем, можно ли ходить на клетку спереди
        if 0 <= y + direction < 8 and self.game.dict_cages[(x, y + direction)].figure is None:
            possible_moves.append((x, y + direction))

            # Если это первый ход пешки, проверяем, можно ли сходить на 2 клетки
            if ((color == "white" and y == 1) or (color == "black" and y == 6)) and self.game.dict_cages[
                (x, y + 2 * direction)].figure is None:
                possible_moves.append((x, y + 2 * direction))

        # Проверяем, можно ли съесть фигуры по диагоналям
        for dx in [-1, 1]:
            if 0 <= x + dx < 8 and 0 <= y + direction < 8:
                target_cage = self.game.dict_cages[(x + dx, y + direction)]
                if target_cage.figure is not None and target_cage.figure.color != color:
                    possible_moves.append((x + dx, y + direction))
        return possible_moves
