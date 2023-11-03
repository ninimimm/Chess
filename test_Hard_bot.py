import copy
import unittest
from HardBot.BotGame import BotGame
from HardBot.Botmain import SharedData
from Server.MovesFigures import MoveFigures
from Server.Cage import Cage
from Server.Figures.Elephant import Elephant
from Server.Figures.Horse import Horse
from Server.Figures.King import King
from Server.Figures.Pawn import Pawn
from Server.Figures.Rook import Rook
from Server.Figures.Queen import Queen
from Server.Game import Game
import threading
import time


class test_Hard_bot(unittest.TestCase): # pragma: no cover
    def test_get_content(self):
        res = None
        def update(dat):
            while bot.is_running:
                if not dat.can_use:
                    data = game.get_possible_moves([dat.copy_field[j][i] for i in range(8) for j in range(8)],
                                                   bot.send_color)
                    push_data = {key: [(int(x.split()[0]), int(x.split()[1])) for x in data[key]] for key in data}
                    dat.game_dict = push_data
                    dat.can_use = True
        def run():
            nonlocal res
            data = game.get_possible_moves([bot.string_images[j][i] for i in range(8) for j in range(8)], "white")
            push_data = {key: [(int(x.split()[0]), int(x.split()[1])) for x in data[key]] for key in data}
            res = bot.get_content(push_data, "white")
        game = Game(90, 80, 140)
        move_figures = MoveFigures(game)
        horse1 = Horse("white", move_figures, game, (1, 0), 0)
        horse2 = Horse("black", move_figures, game, (4, 3), 0)
        king1 = King("white", move_figures, game, (3, 0), 0)
        king2 = King("black", move_figures, game, (3, 7), 0)
        pawn = Pawn("white", move_figures, game, (3, 6), 0)
        pawn1 = Pawn("white", move_figures, game, (4, 7), 0)
        elephant1 = Elephant("black", move_figures, game, (1, 7), 0)
        elephant2 = Elephant("white", move_figures, game, (7, 0), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[horse1.coordinate] = Cage("white", horse1.coordinate, horse1)
        dict_cages[horse2.coordinate] = Cage("black", horse2.coordinate, horse2)
        dict_cages[king1.coordinate] = Cage("white", king1.coordinate, king1)
        dict_cages[king2.coordinate] = Cage("black", king2.coordinate, king2)
        dict_cages[elephant1.coordinate] = Cage("black", elephant1.coordinate, elephant1)
        dict_cages[elephant2.coordinate] = Cage("white", elephant2.coordinate, elephant2)
        dict_cages[pawn.coordinate] = Cage("white", pawn.coordinate, pawn)
        dict_cages[pawn1.coordinate] = Cage("white", pawn.coordinate, pawn1)
        shared_data = SharedData()
        shared_data.game_dict = dict_cages
        bot = BotGame(shared_data)
        bot.string_images = [["None" for _ in range(8)] for _ in range(8)]
        bot.string_images[3][0] = "white_king0"
        bot.string_images[7][0] = "white_elephant0"
        bot.string_images[1][0] = "white_horse0"
        bot.string_images[3][7] = "black_king0"
        bot.string_images[3][6] = "white_pawn0"
        bot.string_images[4][7] = "white_pawn1"
        bot.string_images[4][3] = "black_horse0"
        bot.string_images[1][7] = "black_elephant0"
        shared_data.copy_field = bot.string_images
        move_figures.print_dict_copy(dict_cages)
        bot.is_running = True
        thread1 = threading.Thread(target=run)
        thread2 = threading.Thread(target=update, args=(shared_data, ))
        thread1.start()
        thread2.start()
        thread1.join()
        while bot.is_running:
            continue
        self.assertEqual(res, ((7, 0), (4, 3)))

    def test_get_content_exeption(self):
        res = None

        def update(dat):
            while bot.is_running:
                if not dat.can_use:
                    data = game.get_possible_moves([dat.copy_field[j][i] for i in range(8) for j in range(8)],
                                                   bot.send_color)
                    push_data = {key: [(int(x.split()[0]), int(x.split()[1])) for x in data[key]] for key in data}
                    dat.game_dict = push_data
                    dat.can_use = True

        def run():
            nonlocal res
            data = game.get_possible_moves([bot.string_images[j][i] for i in range(8) for j in range(8)], "white")
            push_data = {key: [(int(x.split()[0]), int(x.split()[1])) for x in data[key]] for key in data}
            res = bot.get_content(push_data, "white")

        game = Game(90, 80, 140)
        move_figures = MoveFigures(game)
        king1 = King("white", move_figures, game, (7, 0), 0)
        king2 = King("black", move_figures, game, (3, 7), 0)
        pawn = Pawn("black", move_figures, game, (2, 0), 0)
        wpawn0 = Pawn("white", move_figures, game, (7, 1), 0)
        wpawn1 = Pawn("white", move_figures, game, (7, 2), 0)
        wpawn2 = Pawn("white", move_figures, game, (6, 0), 0)
        wpawn3 = Pawn("white", move_figures, game, (6, 1), 0)
        wpawn4 = Pawn("white", move_figures, game, (6, 2), 0)
        pawn1 = Pawn("black", move_figures, game, (2, 1), 0)
        pawn2 = Pawn("black", move_figures, game, (4, 1), 0)
        rook = Rook("black", move_figures, game, (3, 5), 0)
        rook1 = Rook("black", move_figures, game, (4, 5), 0)
        queen = Queen("black", move_figures, game, (1, 0), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[pawn2.coordinate] = Cage("black", pawn2.coordinate, pawn2)
        dict_cages[rook1.coordinate] = Cage("black", rook1.coordinate, rook1)
        dict_cages[queen.coordinate] = Cage("black", queen.coordinate, queen)
        dict_cages[king1.coordinate] = Cage("white", king1.coordinate, king1)
        dict_cages[wpawn0.coordinate] = Cage("white", wpawn0.coordinate, wpawn0)
        dict_cages[wpawn1.coordinate] = Cage("white", wpawn1.coordinate, wpawn1)
        dict_cages[wpawn2.coordinate] = Cage("white", wpawn2.coordinate, wpawn2)
        dict_cages[wpawn3.coordinate] = Cage("white", wpawn3.coordinate, wpawn3)
        dict_cages[wpawn4.coordinate] = Cage("white", wpawn4.coordinate, wpawn4)
        dict_cages[king2.coordinate] = Cage("black", king2.coordinate, king2)
        dict_cages[pawn.coordinate] = Cage("black", pawn.coordinate, pawn)
        dict_cages[pawn1.coordinate] = Cage("black", pawn1.coordinate, pawn1)
        dict_cages[rook.coordinate] = Cage("black", rook.coordinate, rook)
        shared_data = SharedData()
        shared_data.game_dict = dict_cages
        bot = BotGame(shared_data)
        bot.string_images = [["None" for _ in range(8)] for _ in range(8)]
        bot.string_images[7][0] = "white_king0"
        bot.string_images[7][1] = "white_pawn0"
        bot.string_images[7][2] = "white_pawn1"
        bot.string_images[6][0] = "white_pawn2"
        bot.string_images[6][1] = "white_pawn3"
        bot.string_images[6][2] = "white_pawn4"
        bot.string_images[3][5] = "black_rook0"
        bot.string_images[3][7] = "black_king0"
        bot.string_images[2][0] = "black_pawn0"
        bot.string_images[2][1] = "black_pawn1"
        bot.string_images[4][1] = "black_pawn2"
        bot.string_images[1][0] = "black_queen0"
        bot.string_images[4][5] = "black_rook1"
        shared_data.copy_field = bot.string_images
        move_figures.print_dict_copy(dict_cages)
        bot.is_running = True
        thread1 = threading.Thread(target=run)
        thread2 = threading.Thread(target=update, args=(shared_data,))
        thread1.start()
        thread2.start()
        thread1.join()
        while bot.is_running:
            continue
        self.assertEqual(True, res in [((6, 2), (6, 3)), ((7, 2), (7, 3))])

    def test_get_content_second_kill(self):
        res = None

        def update(dat):
            while bot.is_running:
                if not dat.can_use:
                    data = game.get_possible_moves([dat.copy_field[j][i] for i in range(8) for j in range(8)],
                                                   bot.send_color)
                    push_data = {key: [(int(x.split()[0]), int(x.split()[1])) for x in data[key]] for key in data}
                    dat.game_dict = push_data
                    dat.can_use = True

        def run():
            nonlocal res
            data = game.get_possible_moves([bot.string_images[j][i] for i in range(8) for j in range(8)], "white")
            push_data = {key: [(int(x.split()[0]), int(x.split()[1])) for x in data[key]] for key in data}
            res = bot.get_content(push_data, "white")

        game = Game(90, 80, 140)
        move_figures = MoveFigures(game)
        king1 = King("white", move_figures, game, (7, 0), 0)
        king2 = King("black", move_figures, game, (7, 7), 0)
        horse1 = Horse("black", move_figures, game, (0, 1), 0)
        horse2 = Horse("black", move_figures, game, (1, 0), 0)
        pawn1 = Pawn("black", move_figures, game, (6, 0), 0)
        pawn2 = Pawn("black", move_figures, game, (7, 1), 0)
        rook = Rook("white", move_figures, game, (0, 0), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[pawn2.coordinate] = Cage("black", pawn2.coordinate, pawn2)
        dict_cages[horse1.coordinate] = Cage("black", horse1.coordinate, horse1)
        dict_cages[horse2.coordinate] = Cage("black", horse2.coordinate, horse2)
        dict_cages[king1.coordinate] = Cage("white", king1.coordinate, king1)
        dict_cages[king2.coordinate] = Cage("black", king2.coordinate, king2)
        dict_cages[pawn1.coordinate] = Cage("black", pawn1.coordinate, pawn1)
        dict_cages[rook.coordinate] = Cage("black", rook.coordinate, rook)
        shared_data = SharedData()
        shared_data.game_dict = dict_cages
        bot = BotGame(shared_data)
        bot.string_images = [["None" for _ in range(8)] for _ in range(8)]
        bot.string_images[7][0] = "white_king0"
        bot.string_images[7][7] = "black_king0"
        bot.string_images[0][1] = "black_horse0"
        bot.string_images[1][0] = "black_horse1"
        bot.string_images[0][0] = "white_rook0"
        bot.string_images[6][0] = "black_pawn0"
        bot.string_images[7][1] = "black_pawn1"
        shared_data.copy_field = bot.string_images
        move_figures.print_dict_copy(dict_cages)
        bot.is_running = True
        thread1 = threading.Thread(target=run)
        thread2 = threading.Thread(target=update, args=(shared_data,))
        thread1.start()
        thread2.start()
        thread1.join()
        while bot.is_running:
            continue
        self.assertEqual(res in [((0, 0), (0, 1)), ((0, 0), (1, 0))], True)
