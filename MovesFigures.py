import copy

from Cage import Cage


class MoveFigures:
    def __init__(self, dict_cages):
        self.dict_cages = dict_cages
        self.dict_figures_moves = {
            "pawn": self.pawn,
            "rook": self.rook,
            "horse": self.horse,
            "elephant": self.elephant,
            "king": self.king,
            "queen": self.queen}

        self.get_attack = {
            "pawn": self.get_pawn,
            "rook": self.get_rook,
            "horse": self.get_horse,
            "elephant": self.get_elephant,
            "king": self.get_king,
            "queen": self.get_queen}

    def draw(self, possible_moves):
        for move in possible_moves:
            self.dict_cages[move].color = "green"

    def pawn(self, coordinate, cage):
        self.draw([x for x in self.get_pawn(coordinate, cage) if x in
                  self.get_possible_defense_moves(cage.figure.color)])

    def get_pawn(self, coordinate, cage):
        x, y = coordinate
        color = cage.figure.color
        direction = 1 if color == "white" else -1  # Направление движения для белых и черных пешек
        possible_moves = []

        # Проверяем, можно ли ходить на клетку спереди
        if 0 <= y + direction < 8 and self.dict_cages[(x, y + direction)].figure is None:
            possible_moves.append((x, y + direction))

            # Если это первый ход пешки, проверяем, можно ли сходить на 2 клетки
            if ((color == "white" and y == 1) or (color == "black" and y == 6)) and self.dict_cages[
                (x, y + 2 * direction)].figure is None:
                possible_moves.append((x, y + 2 * direction))

        # Проверяем, можно ли съесть фигуры по диагоналям
        for dx in [-1, 1]:
            if 0 <= x + dx < 8 and 0 <= y + direction < 8:
                target_cage = self.dict_cages[(x + dx, y + direction)]
                if target_cage.figure is not None and target_cage.figure.color != color:
                    possible_moves.append((x + dx, y + direction))
        return possible_moves

    def rook(self, coordinate, cage):
        self.draw([x for x in self.get_rook(coordinate, cage) if x in
                   self.get_possible_defense_moves(cage.figure.color)])

    def get_rook(self, coordinate, cage):
        x, y = coordinate
        color = cage.figure.color
        possible_moves = []

        # Проверяем возможные ходы вверх
        for dy in range(1, 8):
            if y - dy < 0:
                break
            target_cage = self.dict_cages[(x, y - dy)]
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
            target_cage = self.dict_cages[(x, y + dy)]
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
            target_cage = self.dict_cages[(x - dx, y)]
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
            target_cage = self.dict_cages[(x + dx, y)]
            if target_cage.figure is None:
                possible_moves.append((x + dx, y))
            else:
                if target_cage.figure.color != color:
                    possible_moves.append((x + dx, y))
                break

        return possible_moves

    def horse(self, coordinate, cage):
        self.draw([x for x in self.get_horse(coordinate, cage) if x in
                   self.get_possible_defense_moves(cage.figure.color)])

    def get_horse(self, coordinate, cage):
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
                    possible.append(move)

        return possible

    def elephant(self, coordinate, cage):
        self.draw([x for x in self.get_elephant(coordinate, cage) if x in
                   self.get_possible_defense_moves(cage.figure.color)])

    def get_elephant(self, coordinate, cage):
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
                        possible_moves.append((new_x, new_y))
                    elif target_cage.figure.color != color:
                        possible_moves.append((new_x, new_y))
                        break
                    else:
                        break
                else:
                    break
        return possible_moves

    def king(self, coordinate, cage):
        self.draw([x for x in self.get_king(coordinate, cage) if x in
                   self.get_possible_defense_moves(cage.figure.color)])

    def get_king(self, coordinate, cage):
        x, y = coordinate
        color = cage.figure.color
        possible_moves = [(x + dx, y + dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if dx != 0 or dy != 0]
        possible = []

        for move in possible_moves:
            if 0 <= move[0] < 8 and 0 <= move[1] < 8:
                target_cage = self.dict_cages[move]
                if target_cage.figure is None or target_cage.figure.color != color:
                    possible.append(move)
        return possible

    def queen(self, coordinate, cage):
        self.draw([x for x in self.get_queen(coordinate, cage) if x in
                   self.get_possible_defense_moves(cage.figure.color)])

    def get_queen(self, coordinate, cage):
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
                        possible.append((new_x, new_y))
                    elif target_cage.figure.color != color:
                        possible.append((new_x, new_y))
                        break
                    else:
                        break
                else:
                    break
        return possible

    def get_attack_cages(self, color):
        attack_cages = set()
        for cage in self.dict_cages.values():
            if cage.figure is not None and cage.figure.color != color:
                for cord in self.get_attack[cage.figure.name](cage.coordinate, cage):
                    attack_cages.add(cord)
        return attack_cages

    def is_check(self, color):
        king = [x.coordinate for x in self.dict_cages.values() if x.figure is not None and
                x.figure.name == "king" and x.figure.color == color]
        print(king)
        return king[0] in self.get_attack_cages(color) if len(king) > 0 else False

    def get_possible_defense_moves(self, color):
        possible_defense_moves = set()

        # Получаем все фигуры заданного цвета
        pieces = [cage for cage in self.dict_cages.values() if cage.figure is not None and
                  cage.figure.color == color]

        # Для каждой фигуры получаем возможные ходы атаки
        for piece in pieces:
            attack_moves = self.get_attack[piece.figure.name](piece.coordinate, piece)

            # Проверяем, есть ли ходы для защиты от атаки
            for move in attack_moves:

                current_cage = self.dict_cages[piece.coordinate]
                target_cage = self.dict_cages[move]

                self.dict_cages[move] = current_cage
                self.dict_cages[piece.coordinate] = target_cage

                if not self.is_check(color):
                    possible_defense_moves.add(move)

                self.dict_cages[move] = target_cage
                self.dict_cages[piece.coordinate] = current_cage

        return possible_defense_moves
