import unittest
from Server.Figures.Pawn import Pawn
from Server.Figures.Queen import Queen
from Server.Figures.King import King
from Server.Cage import Cage
from Server.MovesFigures import MoveFigures
from Server.Game import Game

class test_MovesFigures(unittest.TestCase): # pragma: no cover
    def setUp(self):
        self.game = Game(90, 80, 140)
        self.move_figures = MoveFigures(self.game)
        # Здесь вы можете инициализировать необходимые объекты, например, игровое поле и фигуры
        pass

    def test_get_enemy_figures(self):
        pawn_white = Pawn("white", self.move_figures, self.game, (0, 1), 0)
        pawn_black = Pawn("black", self.move_figures, self.game, (0, 6), 0)
        queen_black = Queen("black", self.move_figures, self.game, (5, 5), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[pawn_black.coordinate] = Cage("white", pawn_black.coordinate, pawn_black)
        dict_cages[pawn_white.coordinate] = Cage("white", pawn_white.coordinate, pawn_white)
        dict_cages[queen_black.coordinate] = Cage("white", queen_black.coordinate, queen_black)
        expected_moves = {pawn_black, queen_black}
        self.assertSetEqual(set(self.move_figures.get_enemy_figures(dict_cages, "white")), expected_moves)

    def test_get_enemy_figure_moves(self):
        pawn_white = Pawn("white", self.move_figures, self.game, (0, 1), 0)
        pawn_black = Pawn("black", self.move_figures, self.game, (0, 6), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[pawn_white.coordinate] = Cage("white", pawn_white.coordinate, pawn_white)
        dict_cages[pawn_black.coordinate] = Cage("white", pawn_black.coordinate, pawn_black)
        self.move_figures.dict_figure_moves = {}
        enemy_figures = self.move_figures.get_enemy_figures(dict_cages, "white")
        print(enemy_figures)
        expected_moves = {(0, 5), (0, 4)}
        self.assertSetEqual(set(self.move_figures.get_enemy_figure_moves(enemy_figures[0], dict_cages)), expected_moves)

    def test_is_check_true(self):
        pawn_white = Pawn("white", self.move_figures, self.game, (0, 1), 0)
        king_white = King("white", self.move_figures, self.game, (0, 5), 0)
        queen_black = Queen("black", self.move_figures, self.game, (5, 5), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[pawn_white.coordinate] = Cage("white", pawn_white.coordinate, pawn_white)
        dict_cages[queen_black.coordinate] = Cage("white", queen_black.coordinate, queen_black)
        dict_cages[king_white.coordinate] = Cage("white", king_white.coordinate, king_white)
        self.move_figures.dict_figure_moves = {}
        enemy_figures = self.move_figures.get_enemy_figures(dict_cages, "white")
        tuple = ((0, 1), (0, 3))
        args = enemy_figures, dict_cages, tuple
        self.assertEqual(self.move_figures.is_check(args), True)

    def test_is_check_false(self):
        pawn_white = Pawn("white", self.move_figures, self.game, (0, 1), 0)
        king_white = King("white", self.move_figures, self.game, (0, 6), 0)
        queen_black = Queen("black", self.move_figures, self.game, (5, 5), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[pawn_white.coordinate] = Cage("white", pawn_white.coordinate, pawn_white)
        dict_cages[queen_black.coordinate] = Cage("white", queen_black.coordinate, queen_black)
        dict_cages[king_white.coordinate] = Cage("white", king_white.coordinate, king_white)
        self.move_figures.dict_figure_moves = {}
        enemy_figures = self.move_figures.get_enemy_figures(dict_cages, "white")
        tuple = ((0, 1), (0, 3))
        args = enemy_figures, dict_cages, tuple
        self.assertEqual(self.move_figures.is_check(args), False)

    def test_get_possible_defense_moves_king_check(self):
        pawn_white = Pawn("white", self.move_figures, self.game, (0, 1), 0)
        king_white = King("white", self.move_figures, self.game, (0, 5), 0)
        queen_black = Queen("black", self.move_figures, self.game, (5, 5), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[pawn_white.coordinate] = Cage("white", pawn_white.coordinate, pawn_white)
        dict_cages[queen_black.coordinate] = Cage("white", queen_black.coordinate, queen_black)
        dict_cages[king_white.coordinate] = Cage("white", king_white.coordinate, king_white)
        self.game.current = (king_white.coordinate, dict_cages[king_white.coordinate])
        possible_moves = {(0, 4), (1, 4), (0, 6), (1, 6)}
        self.assertSetEqual(self.move_figures.get_possible_defense_moves("white", dict_cages), possible_moves)

    def test_get_possible_defense_moves_pawn_check(self):
        pawn_white = Pawn("white", self.move_figures, self.game, (0, 1), 0)
        king_white = King("white", self.move_figures, self.game, (0, 5), 0)
        queen_black = Queen("black", self.move_figures, self.game, (5, 5), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[pawn_white.coordinate] = Cage("white", pawn_white.coordinate, pawn_white)
        dict_cages[queen_black.coordinate] = Cage("white", queen_black.coordinate, queen_black)
        dict_cages[king_white.coordinate] = Cage("white", king_white.coordinate, king_white)
        self.game.current = (pawn_white.coordinate, dict_cages[pawn_white.coordinate])
        possible_moves = set()
        self.assertSetEqual(self.move_figures.get_possible_defense_moves("white", dict_cages), possible_moves)

    def test_get_possible_defense_moves_pawn_not_check(self):
        pawn_white = Pawn("white", self.move_figures, self.game, (0, 1), 0)
        king_white = King("white", self.move_figures, self.game, (0, 5), 0)
        queen_black = Queen("black", self.move_figures, self.game, (5, 6), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[pawn_white.coordinate] = Cage("white", pawn_white.coordinate, pawn_white)
        dict_cages[queen_black.coordinate] = Cage("white", queen_black.coordinate, queen_black)
        dict_cages[king_white.coordinate] = Cage("white", king_white.coordinate, king_white)
        self.game.current = (pawn_white.coordinate, dict_cages[pawn_white.coordinate])
        possible_moves = {(0, 2), (0, 3)}
        self.assertSetEqual(self.move_figures.get_possible_defense_moves("white", dict_cages), possible_moves)

    def test_get_possible_defense_moves_king_not_check(self):
        pawn_white = Pawn("white", self.move_figures, self.game, (0, 1), 0)
        king_white = King("white", self.move_figures, self.game, (0, 5), 0)
        queen_black = Queen("black", self.move_figures, self.game, (5, 6), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[pawn_white.coordinate] = Cage("white", pawn_white.coordinate, pawn_white)
        dict_cages[queen_black.coordinate] = Cage("white", queen_black.coordinate, queen_black)
        dict_cages[king_white.coordinate] = Cage("white", king_white.coordinate, king_white)
        self.game.current = (king_white.coordinate, dict_cages[king_white.coordinate])
        possible_moves = {(1, 5), (1, 4), (0, 4)}
        self.assertSetEqual(self.move_figures.get_possible_defense_moves("white", dict_cages), possible_moves)

if __name__ == '__main__': # pragma: no cover
    unittest.main()