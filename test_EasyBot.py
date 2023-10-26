import copy
import unittest
from EasyBot.EasyBotGame import EasyBotGame
from EasyBot.EasyBotmain import SharedData
from Server.MovesFigures import MoveFigures
from Server.Cage import Cage
from Server.Figures.Elephant import Elephant
from Server.Figures.Horse import Horse
from Server.Figures.King import King
from Server.Game import Game
import threading
import time


class test_EasyBot(unittest.TestCase): # pragma: no cover
    def test_get_content(self):
        res = None
        def update(dat):
            while bot.is_running:
                if not dat.can_use:
                    data = game.get_possible_moves([bot.string_images[j][i] for i in range(8) for j in range(8)],
                                                   "black")
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
        elephant1 = Elephant("black", move_figures, game, (1, 7), 0)
        elephant2 = Elephant("white", move_figures, game, (7, 0), 0)
        dict_cages = {(x, y): Cage("white", (x, y)) for x in range(8) for y in range(8)}
        dict_cages[horse1.coordinate] = Cage("white", horse1.coordinate, horse1)
        dict_cages[horse2.coordinate] = Cage("black", horse2.coordinate, horse2)
        dict_cages[king1.coordinate] = Cage("white", king1.coordinate, king1)
        dict_cages[king2.coordinate] = Cage("black", king2.coordinate, king2)
        dict_cages[elephant1.coordinate] = Cage("black", elephant1.coordinate, elephant1)
        dict_cages[elephant2.coordinate] = Cage("white", elephant2.coordinate, elephant2)
        shared_data = SharedData()
        shared_data.game_dict = dict_cages
        bot = EasyBotGame(shared_data)
        bot.string_images = [["None" for _ in range(8)] for _ in range(8)]
        bot.string_images[3][0] = "white_king0"
        bot.string_images[7][0] = "white_elephant0"
        bot.string_images[1][0] = "white_horse0"
        bot.string_images[3][7] = "black_king0"
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
        time.sleep(1)
        while bot.is_running:
            continue
        print("fasfdas")
        self.assertEqual(res, ((7, 0), (4, 3)))