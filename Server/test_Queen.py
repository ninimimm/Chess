import unittest
from Figures.Queen import Queen
from Cage import Cage
from MovesFigures import MoveFigures
from Game import Game

class test_Queen(unittest.TestCase):
    def setUp(self):
        self.game = Game(90, 80, 140)
        self.move_figures = MoveFigures(self.game)
        # Здесь вы можете инициализировать необходимые объекты, например, игровое поле и фигуры
        pass

    def test_get_moves_empty_board_full_clear(self):
        queen = Queen("white", self.move_figures, self.game, (2, 2), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[queen.coordinate] = Cage("white", queen.coordinate, queen)
        moves = queen.get_moves((2, 2), dict_cages[(2, 2)], dict_cages)
        expected_moves = {(0, 0), (0, 2), (1, 1), (1, 2), (2, 0), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
                          (3, 1), (3, 2), (3, 3), (4, 0), (4, 2), (4, 4), (5, 2), (5, 5), (6, 2), (6, 6), (7, 2), (7, 7),
                          (1, 3), (0, 4)}
        self.assertSetEqual(set(moves), expected_moves)

    def test_get_moves_with_blocking_our_figure(self):
        queen = Queen("white", self.move_figures, self.game, (0, 0), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[queen.coordinate] = Cage("white", queen.coordinate, queen)
        queen1 = Queen("white", self.move_figures, self.game, (0, 1), 1)
        dict_cages[queen1.coordinate] = Cage("white", queen1.coordinate, queen1)
        moves = queen.get_moves((0, 0), dict_cages[(0, 0)], dict_cages)
        expected_moves = {(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
                          (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)}
        self.assertSetEqual(set(moves), expected_moves)

    def test_get_moves_with_blocking_enemy_figure(self):
        queen = Queen("white", self.move_figures, self.game, (0, 0), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[queen.coordinate] = Cage("white", queen.coordinate, queen)
        queen1 = Queen("black", self.move_figures, self.game, (0, 1), 1)
        dict_cages[queen1.coordinate] = Cage("white", queen1.coordinate, queen1)
        moves = queen.get_moves((0, 0), dict_cages[(0, 0)], dict_cages)
        expected_moves = {(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
                          (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (0, 1)}
        self.assertSetEqual(set(moves), expected_moves)

if __name__ == '__main__':
    unittest.main()
