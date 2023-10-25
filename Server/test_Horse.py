import unittest
from Figures.Horse import Horse
from Cage import Cage
from MovesFigures import MoveFigures
from Game import Game

class test_Horse(unittest.TestCase):
    def setUp(self):
        self.game = Game(90, 80, 140)
        self.move_figures = MoveFigures(self.game)
        # Здесь вы можете инициализировать необходимые объекты, например, игровое поле и фигуры
        pass

    def test_get_moves_empty_board_full_clear(self):
        horse = Horse("white", self.move_figures, self.game, (2, 2), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[horse.coordinate] = Cage("white", horse.coordinate, horse)
        moves = horse.get_moves((2, 2), dict_cages[(2, 2)], dict_cages)
        expected_moves = {(0, 1), (1, 0), (0, 3), (3, 0), (1, 4), (4, 1), (3, 4), (4, 3)}
        self.assertSetEqual(set(moves), expected_moves)

    def test_get_moves_empty_board_in_corner(self):
        horse = Horse("white", self.move_figures, self.game, (0, 0), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[horse.coordinate] = Cage("white", horse.coordinate, horse)
        moves = horse.get_moves((0, 0), dict_cages[(0, 0)], dict_cages)
        expected_moves = {(2, 1), (1, 2)}
        self.assertSetEqual(set(moves), expected_moves)

    def test_get_moves_empty_board_one_step_corner(self):
        horse = Horse("white", self.move_figures, self.game, (1, 0), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[horse.coordinate] = Cage("white", horse.coordinate, horse)
        moves = horse.get_moves((1, 0), dict_cages[(1, 0)], dict_cages)
        expected_moves = {(0, 2), (2, 2), (3, 1)}
        self.assertSetEqual(set(moves), expected_moves)

    def test_get_moves_empty_board_near_wall(self):
        horse = Horse("white", self.move_figures, self.game, (2, 0), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[horse.coordinate] = Cage("white", horse.coordinate, horse)
        moves = horse.get_moves((2, 0), dict_cages[(2, 0)], dict_cages)
        expected_moves = {(0, 1), (1, 2), (3, 2), (4, 1)}
        self.assertSetEqual(set(moves), expected_moves)

    def test_get_moves_with_blocking_our_figure(self):
        horse = Horse("white", self.move_figures, self.game, (2, 2), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[horse.coordinate] = Cage("white", horse.coordinate, horse)
        horse1 = Horse("white", self.move_figures, self.game, (3, 0), 1)
        dict_cages[horse1.coordinate] = Cage("white", horse1.coordinate, horse1)
        moves = horse.get_moves((2, 2), dict_cages[(2, 2)], dict_cages)
        expected_moves = {(0, 1), (1, 0), (0, 3), (1, 4), (4, 1), (3, 4), (4, 3)}
        self.assertSetEqual(set(moves), expected_moves)

    def test_get_moves_with_blocking_enemy_figure(self):
        horse = Horse("white", self.move_figures, self.game, (2, 2), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[horse.coordinate] = Cage("white", horse.coordinate, horse)
        horse1 = Horse("black", self.move_figures, self.game, (3, 0), 1)
        dict_cages[horse1.coordinate] = Cage("black", horse1.coordinate, horse1)
        moves = horse.get_moves((2, 2), dict_cages[(2, 2)], dict_cages)
        expected_moves = {(0, 1), (1, 0), (0, 3), (3, 0), (1, 4), (4, 1), (3, 4), (4, 3)}
        self.assertSetEqual(set(moves), expected_moves)

if __name__ == '__main__':
    unittest.main()
