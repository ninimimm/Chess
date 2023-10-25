import unittest
from Figures.Elephant import Elephant
from Cage import Cage
from MovesFigures import MoveFigures
from Game import Game

class test_Elephant(unittest.TestCase): # pragma: no cover
    def setUp(self):
        self.game = Game(90, 80, 140)
        self.move_figures = MoveFigures(self.game)
        # Здесь вы можете инициализировать необходимые объекты, например, игровое поле и фигуры
        pass

    def test_get_moves_empty_board(self):
        elephant = Elephant("white", self.move_figures, self.game, (2, 2), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[elephant.coordinate] = Cage("white", elephant.coordinate, elephant)
        moves = elephant.get_moves((2, 2), dict_cages[(2, 2)], dict_cages)
        expected_moves = {(0, 0), (1, 1), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (3, 1), (4, 0), (1, 3), (0, 4)}
        self.assertSetEqual(set(moves), expected_moves)

    def test_get_moves_with_blocking_our_figure(self):
        elephant = Elephant("white", self.move_figures, self.game, (2, 2), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[elephant.coordinate] = Cage("white", elephant.coordinate, elephant)
        elephant = Elephant("white", self.move_figures, self.game, (4, 4), 0)
        dict_cages[elephant.coordinate] = Cage("white", elephant.coordinate, elephant)
        moves = elephant.get_moves((2, 2), dict_cages[(2, 2)], dict_cages)
        expected_moves = {(0, 0), (1, 1), (3, 3), (3, 1), (4, 0), (1, 3), (0, 4)}
        self.assertSetEqual(set(moves), expected_moves)

    def test_get_moves_with_blocking_enemy_figure(self):
        elephant = Elephant("white", self.move_figures, self.game, (2, 2), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[elephant.coordinate] = Cage("white", elephant.coordinate, elephant)
        elephant = Elephant("black", self.move_figures, self.game, (4, 4), 0)
        dict_cages[elephant.coordinate] = Cage("white", elephant.coordinate, elephant)
        moves = elephant.get_moves((2, 2), dict_cages[(2, 2)], dict_cages)
        expected_moves = {(0, 0), (1, 1), (3, 3), (3, 1), (4, 0), (1, 3), (0, 4), (4, 4)}
        self.assertSetEqual(set(moves), expected_moves)

if __name__ == '__main__': # pragma: no cover
    unittest.main()
