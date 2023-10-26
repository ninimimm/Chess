import unittest
from Figures.Horse import Horse
from Cage import Cage
from MovesFigures import MoveFigures
from Game import Game

class test_Pawn(unittest.TestCase): # pragma: no cover
    def setUp(self):
        self.game = Game(90, 80, 140)
        self.move_figures = MoveFigures(self.game)
        # Здесь вы можете инициализировать необходимые объекты, например, игровое поле и фигуры
        pass

    def test_get_new_dict_all_none(self):
        figures = ["None" for _ in range(64)]
        self.assertEqual(
            sum([1 if x.figure is None else 0
                 for x in self.game.get_new_dict(figures).values()]), 64)

    def test_get_new_dict_default(self):
        figures = ["None" for _ in range(64)]
        figures[6] = "white_pawn0"
        self.assertEqual(
            sum([1 if x.figure is None else 0
                 for x in self.game.get_new_dict(figures).values()]), 63)

    def test_create_figure_queen(self):
        name = "Queen"
        coordinate = (5, 5)
        self.game.players_ip["123.123.123.123"] = ("white", True)
        self.game.create_figure(name, coordinate, "123.123.123.123")
        self.assertEqual((self.game.dict_cages[coordinate].figure.name,
                          self.game.dict_cages[coordinate].figure.coordinate),
                         ("queen", (5, 5)))

    def test_create_figure_horse(self):
        name = "Horse"
        coordinate = (3, 7)
        self.game.players_ip["123.123.123.123"] = ("white", True)
        self.game.create_figure(name, coordinate, "123.123.123.123")
        self.assertEqual((self.game.dict_cages[coordinate].figure.name,
                          self.game.dict_cages[coordinate].figure.coordinate),
                         ("horse", (3, 7)))

    def test_create_figure_elephant(self):
        name = "Elephant"
        horse = Horse("white", self.move_figures, self.game, (1, 7), 0)
        self.game.white_player.figures[6] = Cage("white", horse.coordinate, horse)
        coordinate = (1, 7)
        self.game.players_ip["123.123.123.123"] = ("white", False)
        self.game.create_figure(name, coordinate, "123.123.123.123")
        self.assertEqual((self.game.dict_cages[coordinate].figure.name,
                          self.game.dict_cages[coordinate].figure.coordinate),
                         ("elephant", (1, 7)))

    def test_create_figure_rook(self):
        name = "Rook"
        coordinate = (0, 0)
        horse = Horse("black", self.move_figures, self.game, (0, 0), 0)
        self.game.black_player.figures[6] = Cage("white", horse.coordinate, horse)
        self.game.players_ip["123.123.123.123"] = ("black", True)
        self.game.create_figure(name, coordinate, "123.123.123.123")
        self.assertEqual((self.game.dict_cages[coordinate].figure.name,
                          self.game.dict_cages[coordinate].figure.coordinate),
                         ("rook", (0, 0)))
    def test_get_response(self):
        self.game.dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        horse = Horse("white", self.move_figures, self.game, (2, 2), 0)
        self.game.dict_cages[horse.coordinate] = Cage("white", horse.coordinate, horse)
        address = "123.123.123.123"
        self.game.players_ip[address] = ("white", True)
        string = self.game.get_response(address)
        equal = [x.figure.name if x.figure is not None else "None" for x in self.game.dict_cages.values()]
        equal[horse.coordinate[1]*8 + horse.coordinate[0]] = "horse"
        self.assertEqual((string.split(',')[0].split(),
                          [x.split('_')[1][:-1] if x != "None" else "None" for x in string.split(',')[1].split()]),
                         ([x.color for x in self.game.dict_cages.values()],
                          equal))


if __name__ == '__main__': # pragma: no cover
    unittest.main()