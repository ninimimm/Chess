import unittest
from Figures.Pawn import Pawn
from Cage import Cage
from MovesFigures import MoveFigures
from Game import Game

class test_Pawn(unittest.TestCase):
    def setUp(self):
        self.game = Game(90, 80, 140)
        self.move_figures = MoveFigures(self.game)
        # Здесь вы можете инициализировать необходимые объекты, например, игровое поле и фигуры
        pass

    def test_get_moves_empty_board_start_position(self):
        pawn = Pawn("white", self.move_figures, self.game, (0, 1), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[pawn.coordinate] = Cage("white", pawn.coordinate, pawn)
        moves = pawn.get_moves((0, 1), dict_cages[(0, 1)], dict_cages)
        expected_moves = {(0, 2), (0, 3)}
        self.assertSetEqual(set(moves), expected_moves)

    def test_get_moves_empty_board_second_position(self):
        pawn = Pawn("white", self.move_figures, self.game, (0, 2), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[pawn.coordinate] = Cage("white", pawn.coordinate, pawn)
        moves = pawn.get_moves((0, 2), dict_cages[(0, 2)], dict_cages)
        expected_moves = {(0, 3)}
        self.assertSetEqual(set(moves), expected_moves)

    def test_get_moves_empty_board_third_position(self):
        pawn = Pawn("white", self.move_figures, self.game, (0, 3), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[pawn.coordinate] = Cage("white", pawn.coordinate, pawn)
        moves = pawn.get_moves((0, 3), dict_cages[(0, 3)], dict_cages)
        expected_moves = {(0, 4)}
        self.assertSetEqual(set(moves), expected_moves)

    def test_get_moves_with_block_our_figure(self):
        pawn = Pawn("white", self.move_figures, self.game, (2, 2), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[pawn.coordinate] = Cage("white", pawn.coordinate, pawn)
        pawn1 = Pawn("white", self.move_figures, self.game, (2, 3), 1)
        dict_cages[pawn1.coordinate] = Cage("white", pawn1.coordinate, pawn1)
        moves = pawn.get_moves((2, 2), dict_cages[(2, 2)], dict_cages)
        expected_moves = []
        self.assertEqual(moves, expected_moves)

    def test_get_moves_with_block_enemy_figure(self):
        pawn = Pawn("white", self.move_figures, self.game, (2, 2), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[pawn.coordinate] = Cage("white", pawn.coordinate, pawn)
        pawn1 = Pawn("black", self.move_figures, self.game, (2, 3), 1)
        dict_cages[pawn1.coordinate] = Cage("white", pawn1.coordinate, pawn1)
        moves = pawn.get_moves((2, 2), dict_cages[(2, 2)], dict_cages)
        expected_moves = []
        self.assertEqual(moves, expected_moves)

    def test_get_moves_with_block_kill_enemy_figure(self):
        pawn = Pawn("white", self.move_figures, self.game, (2, 2), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[pawn.coordinate] = Cage("white", pawn.coordinate, pawn)
        pawn1 = Pawn("black", self.move_figures, self.game, (1, 3), 1)
        dict_cages[pawn1.coordinate] = Cage("white", pawn1.coordinate, pawn1)
        moves = pawn.get_moves((2, 2), dict_cages[(2, 2)], dict_cages)
        expected_moves = {(1, 3), (2, 3)}
        self.assertSetEqual(set(moves), expected_moves)

    def test_get_moves_with_block_kill_our_figure(self):
        pawn = Pawn("white", self.move_figures, self.game, (2, 2), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[pawn.coordinate] = Cage("white", pawn.coordinate, pawn)
        pawn1 = Pawn("white", self.move_figures, self.game, (1, 3), 1)
        dict_cages[pawn1.coordinate] = Cage("white", pawn1.coordinate, pawn1)
        moves = pawn.get_moves((2, 2), dict_cages[(2, 2)], dict_cages)
        expected_moves = {(2, 3)}
        self.assertSetEqual(set(moves), expected_moves)

if __name__ == '__main__':
    unittest.main()
