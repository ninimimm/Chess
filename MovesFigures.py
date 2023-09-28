from Cage import Cage

class MoveFigures:
    def __init__(self, dict_cages):
        self.dict_cages = dict_cages
        self.dict_figures_moves = {
            "pawn": self.move_pawn,
            "rook": self.move_rook,
            "horse": self.move_horse,
            "elephant": self.move_elephant,
            "king": self.move_king,
            "queen": self.move_queen}

    def move_pawn(self, coordinate, cage):
        x, y = coordinate
        color = cage.figure.color
        direction = 1 if color == "white" else -1  # Направление движения для белых и черных пешек
        possible_moves = []

        # Проверяем, можно ли ходить на клетку спереди
        if 0 <= y + direction < 8 and self.dict_cages[(x, y + direction)].figure is None:
            possible_moves.append((x, y + direction))
            self.dict_cages[(x, y + direction)].color = "green"

            # Если это первый ход пешки, проверяем, можно ли сходить на 2 клетки
            if ((color == "white" and y == 1) or (color == "black" and y == 6)) and self.dict_cages[
                (x, y + 2 * direction)].figure is None:
                self.dict_cages[(x, y + 2 * direction)].color = "green"
                possible_moves.append((x, y + 2 * direction))

        # Проверяем, можно ли съесть фигуры по диагоналям
        for dx in [-1, 1]:
            if 0 <= x + dx < 8 and 0 <= y + direction < 8:
                target_cage = self.dict_cages[(x + dx, y + direction)]
                possible_moves.append((x + dx, y + direction))
                if target_cage.figure is not None and target_cage.figure.color != color:
                    target_cage.color = "green"
        return possible_moves

    def move_rook(self, coordinate, cage):
        x, y = coordinate
        color = cage.figure.color
        possible_moves = []

        # Проверяем возможные ходы вверх
        for dy in range(1, 8):
            if y - dy < 0:
                break
            target_cage = self.dict_cages[(x, y - dy)]
            if target_cage.figure is None:
                target_cage.color = "green"
                possible_moves.append((x, y - dy))
            else:
                if target_cage.figure.color != color:
                    target_cage.color = "green"
                    possible_moves.append((x, y - dy))
                break

        # Проверяем возможные ходы вниз
        for dy in range(1, 8):
            if y + dy >= 8:
                break
            target_cage = self.dict_cages[(x, y + dy)]
            if target_cage.figure is None:
                target_cage.color = "green"
                possible_moves.append((x, y + dy))
            else:
                if target_cage.figure.color != color:
                    target_cage.color = "green"
                    possible_moves.append((x, y + dy))
                break

        # Проверяем возможные ходы влево
        for dx in range(1, 8):
            if x - dx < 0:
                break
            target_cage = self.dict_cages[(x - dx, y)]
            if target_cage.figure is None:
                target_cage.color = "green"
                possible_moves.append((x - dx, y))
            else:
                if target_cage.figure.color != color:
                    target_cage.color = "green"
                    possible_moves.append((x - dx, y))
                break

        # Проверяем возможные ходы вправо
        for dx in range(1, 8):
            if x + dx >= 8:
                break
            target_cage = self.dict_cages[(x + dx, y)]
            if target_cage.figure is None:
                target_cage.color = "green"
                possible_moves.append((x + dx, y))
            else:
                if target_cage.figure.color != color:
                    target_cage.color = "green"
                    possible_moves.append((x + dx, y))
                break

        return possible_moves
    def move_horse(self, coordinate, cage):
        x, y = coordinate
        color = cage.figure.color
        possible_moves = [
            (x + 2, y + 1), (x + 2, y - 1),
            (x - 2, y + 1), (x - 2, y - 1),
            (x + 1, y + 2), (x + 1, y - 2),
            (x - 1, y + 2), (x - 1, y - 2)
        ]
        possible = []

        for move in possible_moves:
            if 0 <= move[0] < 8 and 0 <= move[1] < 8:
                target_cage = self.dict_cages[move]
                if target_cage.figure is None or target_cage.figure.color != color:
                    target_cage.color = "green"
                    possible.append(move)

        return possible


    def move_elephant(self, coordinate, cage):
        x, y = coordinate
        color = cage.figure.color
        directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
        possible_moves = []

        for dx, dy in directions:
            for i in range(1, 8):
                new_x, new_y = x + i * dx, y + i * dy
                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    target_cage = self.dict_cages[(new_x, new_y)]
                    if target_cage.figure is None:
                        target_cage.color = "green"
                        possible_moves.append((new_x, new_y))
                    elif target_cage.figure.color != color:
                        target_cage.color = "green"
                        possible_moves.append((new_x, new_y))
                        break
                    else:
                        break
                else:
                    break
        return possible_moves

    def move_king(self, coordinate, cage):
        x, y = coordinate
        color = cage.figure.color
        possible_moves = [(x + dx, y + dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if dx != 0 or dy != 0]
        possible = []

        for move in possible_moves:
            if 0 <= move[0] < 8 and 0 <= move[1] < 8:
                target_cage = self.dict_cages[move]
                if target_cage.figure is None or target_cage.figure.color != color:
                    target_cage.color = "green"
                    possible.append(move)
        return possible

    def move_queen(self, coordinate, cage):
        x, y = coordinate
        color = cage.figure.color
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        possible = []

        for dx, dy in directions:
            for i in range(1, 8):
                new_x, new_y = x + i * dx, y + i * dy
                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    target_cage = self.dict_cages[(new_x, new_y)]
                    if target_cage.figure is None:
                        target_cage.color = "green"
                        possible.append((new_x, new_y))
                    elif target_cage.figure.color != color:
                        target_cage.color = "green"
                        possible.append((new_x, new_y))
                        break
                    else:
                        break
                else:
                    break
        return possible

