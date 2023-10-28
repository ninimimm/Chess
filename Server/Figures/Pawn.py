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

    def __str__(self): # pragma: no cover
        return f"{self.name[0]},{self.color[0]},{self.coordinate}"

    def moves(self, cage, dict_cages): # pragma: no cover
        self.move_figures.draw(self.get_possible_moves(cage, dict_cages))

    def get_possible_moves(self, cage, dict_cages): # pragma: no cover
        return list(self.move_figures.get_possible_defense_moves(cage.figure.color, dict_cages))

    def get_moves(self, coordinate, cage, dict_cages):
        x, y = coordinate
        color = cage.figure.color
        direction = 1 if color == "white" else -1  # Направление движения для белых и черных пешек
        possible_moves = set()
        # Проверяем, можно ли ходить на клетку спереди
        if 0 <= y + direction < 8 and dict_cages[(x, y + direction)].figure is None:
            possible_moves.add((x, y + direction))

            # Если это первый ход пешки, проверяем, можно ли сходить на 2 клетки
            if ((color == "white" and y == 1) or (color == "black" and y == 6)) and dict_cages[
                (x, y + 2 * direction)].figure is None:
                possible_moves.add((x, y + 2 * direction))

        # Проверяем, можно ли съесть фигуры по диагоналям
        for dx in [-1, 1]:
            if 0 <= x + dx < 8 and 0 <= y + direction < 8:
                target_cage = dict_cages[(x + dx, y + direction)]
                if target_cage.figure is not None and target_cage.figure.color != color:
                    possible_moves.add((x + dx, y + direction))

        if x == 3 or x == 4:
            right_coordinate, left_coordinate = (x + 1, y), (x - 1, y)
            if dict_cages[right_coordinate] is not None and dict_cages[right_coordinate].figure is not None and dict_cages[right_coordinate].figure.name == "pawn":
                print(right_coordinate)
                print(dict_cages[right_coordinate])
                print(dict_cages[right_coordinate].figure.last_move)
            right_cage, left_cage = dict_cages[right_coordinate], dict_cages[left_coordinate]
            if right_cage.figure is not None and right_cage.figure.name == "pawn" and right_cage.figure.color != color\
                    and self.game.last_move == (x + 1, y + 2 * direction):
                possible_moves.add((x + 1, y + 1 * direction))
            if left_cage.figure is not None and left_cage.figure.name == "pawn" and left_cage.figure.color != color\
                    and self.game.last_move == (x - 1, y + 2 * direction):
                possible_moves.add((x - 1, y + 1 * direction))
        return possible_moves
