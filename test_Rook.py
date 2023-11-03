import unittest
from Server.Figures.Rook import Rook
from Server.Cage import Cage
from Server.MovesFigures import MoveFigures
from Server.Game import Game

class test_Queen(unittest.TestCase): # pragma: no cover
    def setUp(self):
        self.game = Game(90, 80, 140)
        self.move_figures = MoveFigures(self.game)
        # Здесь вы можете инициализировать необходимые объекты, например, игровое поле и фигуры
        pass

    def test_get_moves_empty_board_full_clear(self):
        rook = Rook("white", self.move_figures, self.game, (2, 2), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[rook.coordinate] = Cage("white", rook.coordinate, rook)
        moves = rook.get_moves((2, 2), dict_cages[(2, 2)], dict_cages)
        expected_moves = {(2, 0), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
                          (0, 2), (1, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2)}
        self.assertSetEqual(set(moves), expected_moves)

    def test_get_moves_with_blocking_our_figure(self):
        rook = Rook("white", self.move_figures, self.game, (0, 0), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[rook.coordinate] = Cage("white", rook.coordinate, rook)
        rook1 = Rook("white", self.move_figures, self.game, (0, 1), 1)
        dict_cages[rook1.coordinate] = Cage("white", rook1.coordinate, rook1)
        moves = rook.get_moves((0, 0), dict_cages[(0, 0)], dict_cages)
        expected_moves = {(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)}
        self.assertSetEqual(set(moves), expected_moves)

    def test_get_moves_with_blocking_enemy_figure_down(self):
        rook = Rook("white", self.move_figures, self.game, (0, 0), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[rook.coordinate] = Cage("white", rook.coordinate, rook)
        rook1 = Rook("black", self.move_figures, self.game, (1, 0), 1)
        dict_cages[rook1.coordinate] = Cage("white", rook1.coordinate, rook1)
        moves = rook.get_moves((0, 0), dict_cages[(0, 0)], dict_cages)
        expected_moves = {(1, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)}
        self.assertSetEqual(set(moves), expected_moves)

    def test_get_moves_with_blocking_enemy_figure_left(self):
        rook = Rook("white", self.move_figures, self.game, (0, 1), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[rook.coordinate] = Cage("white", rook.coordinate, rook)
        rook1 = Rook("black", self.move_figures, self.game, (0, 0), 1)
        dict_cages[rook1.coordinate] = Cage("white", rook1.coordinate, rook1)
        moves = rook.get_moves((0, 1), dict_cages[(0, 1)], dict_cages)
        expected_moves = {(0, 0), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1),
                          (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)}
        self.assertSetEqual(set(moves), expected_moves)
    def test_get_moves_with_blocking_enemy_figure_right(self):
        rook = Rook("white", self.move_figures, self.game, (0, 1), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[rook.coordinate] = Cage("white", rook.coordinate, rook)
        rook1 = Rook("black", self.move_figures, self.game, (0, 2), 1)
        dict_cages[rook1.coordinate] = Cage("white", rook1.coordinate, rook1)
        moves = rook.get_moves((0, 1), dict_cages[(0, 1)], dict_cages)
        expected_moves = {(0, 0), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1),
                          (0, 2)}
        self.assertSetEqual(set(moves), expected_moves)
    def test_get_moves_with_blocking_enemy_figure_up(self):
        rook = Rook("white", self.move_figures, self.game, (1, 1), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[rook.coordinate] = Cage("white", rook.coordinate, rook)
        rook1 = Rook("black", self.move_figures, self.game, (0, 1), 1)
        dict_cages[rook1.coordinate] = Cage("white", rook1.coordinate, rook1)
        moves = rook.get_moves((1, 1), dict_cages[(1, 1)], dict_cages)
        expected_moves = {(0, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1),
                          (1, 0), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)}
        self.assertSetEqual(set(moves), expected_moves)

if __name__ == '__main__': # pragma: no cover
    unittest.main()
