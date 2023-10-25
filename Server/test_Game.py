import unittest
from Figures.Pawn import Pawn
from Cage import Cage
from MovesFigures import MoveFigures
from Game import Game

class test_Pawn(unittest.TestCase): # pragma: no cover
    def setUp(self):
        self.game = Game(90, 80, 140)
        self.move_figures = MoveFigures(self.game)
        # Здесь вы можете инициализировать необходимые объекты, например, игровое поле и фигуры
        pass

    def test_get_moves_empty_board_start_position(self):
        pass

if __name__ == '__main__': # pragma: no cover
    unittest.main()