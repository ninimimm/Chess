import unittest
from Figures.King import King
from Figures.Elephant import Elephant
from Cage import Cage
from MovesFigures import MoveFigures
from Game import Game

class test_King(unittest.TestCase):
    def setUp(self):
        self.game = Game(90, 80, 140)
        self.move_figures = MoveFigures(self.game)
        # Здесь вы можете инициализировать необходимые объекты, например, игровое поле и фигуры
        pass

    def test_get_moves_empty_board_full_clear(self):
        king = King("white", self.move_figures, self.game, (2, 2), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[king.coordinate] = Cage("white", king.coordinate, king)
        moves = king.get_moves((2, 2), dict_cages[(2, 2)], dict_cages)
        expected_moves = {(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (2, 1)}
        self.assertSetEqual(set(moves), expected_moves)

    def test_get_moves_empty_board_in_corner(self):
        king = King("white", self.move_figures, self.game, (0, 0), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[king.coordinate] = Cage("white", king.coordinate, king)
        moves = king.get_moves((0, 0), dict_cages[(0, 0)], dict_cages)
        expected_moves = {(0, 1), (1, 0), (1, 1)}
        self.assertSetEqual(set(moves), expected_moves)

    def test_get_moves_empty_board_one_step_corner(self):
        king = King("white", self.move_figures, self.game, (1, 0), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[king.coordinate] = Cage("white", king.coordinate, king)
        moves = king.get_moves((1, 0), dict_cages[(1, 0)], dict_cages)
        expected_moves = {(0, 0), (0, 1), (1, 1), (2, 0), (2, 1)}
        self.assertSetEqual(set(moves), expected_moves)

    def test_get_moves_with_blocking_our_figure(self):
        king = King("white", self.move_figures, self.game, (2, 2), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[king.coordinate] = Cage("white", king.coordinate, king)
        elephant = Elephant("white", self.move_figures, self.game, (2, 1), 1)
        dict_cages[elephant.coordinate] = Cage("white", elephant.coordinate, elephant)
        moves = king.get_moves((2, 2), dict_cages[(2, 2)], dict_cages)
        expected_moves = {(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1)}
        self.assertSetEqual(set(moves), expected_moves)

    def test_get_moves_with_blocking_enemy_figure(self):
        horse = King("white", self.move_figures, self.game, (2, 2), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[horse.coordinate] = Cage("white", horse.coordinate, horse)
        horse1 = King("black", self.move_figures, self.game, (3, 0), 0)
        dict_cages[horse1.coordinate] = Cage("black", horse1.coordinate, horse1)
        moves = horse.get_moves((2, 2), dict_cages[(2, 2)], dict_cages)
        expected_moves = {(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (2, 1)}
        self.assertSetEqual(set(moves), expected_moves)

if __name__ == '__main__':
    unittest.main()
