import socket
import select
import threading
from BotGame import BotGame
from concurrent.futures import ThreadPoolExecutor
class SharedData:
    def __init__(self):
        self.coordinate = None
        self.game = None
        self.answer_button = None
        self.copy_field = None

# Создаем единственный экземпляр SharedData
shared_data = SharedData()
gui = None

# В ваших потоках используйте shared_data.coordinate и shared_data.gam
if __name__ == "__main__":
    def run_start():
        global gui
        shared_data.game = BotGame(shared_data)
    def connection():
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('178.154.244.233', 8080))
        print("Отправил первичный запрос")
        client.sendall("0 7".encode('utf-8'))
        while True:
            if shared_data.game.send_color is not None:
               print(shared_data.copy_field)
               client.sendall(f"possible moves,{' '.join([x[j] for j in range(8) for x in shared_data.copy_field])},{shared_data.game.color}".encode('utf-8'))
               shared_data.game.send_color = None
            ready = select.select([client], [], [], 0.05)
            if ready[0]:
                print("Получил ответ от сервера")
                data = client.recv(1024).decode('utf-8')
                if len(data) > 0:
                    if "possible moves" in data:
                        parse = data[14:].split(",")
                        game_dict = {}
                        for item in parse:
                            item_parse = item.split(":")
                            key = [int(x) for x in item_parse[0].split()]
                            game_dict[(key[0], key[1])] = [(int(x.split()[0]), int(x.split()[1])) for x in item_parse[1].split('|')]
                        if not shared_data.game.get_content.is_running():
                            with ThreadPoolExecutor() as executor:
                                thread = executor.submit(shared_data.game.get_content, game_dict, shared_data.game.send_color)
                                incoming, outcoming = thread.result()
                                client.sendall(f"{incoming[0]} {incoming[1]}".encode('utf-8'))
                                client.recv(1024).decode('utf-8')
                                client.sendall(f"{outcoming[0]} {outcoming[1]}".encode('utf-8'))
                                client.recv(1024).decode('utf-8')
                        # thread3 = threading.Thread(target=shared_data.game.get_content, args=[game_dict, shared_data.game.send_color])
                        # thread3.start()
                        
                    elif data.split()[0] == "choice":
                        gui.game.choose_figure(data.split()[1])
                        while shared_data.answer_button is None:
                            continue
                        print("Отправил запрос на сервер")
                        client.sendall(shared_data.answer_button.encode('utf-8'))
                        shared_data.answer_button = None
                    else:
                        print(data)
                        parse = data.split(" ,")
                        if parse[0] == "None":
                            cages = "None"
                        else:
                            cages = [x for x in parse[0].split()]
                        figures = [x for x in parse[1].split()]
                        for i in range(8):
                            for j in range(8):
                                shared_data.game.string_images[j][i] = figures[i * 8 + j]
                        print(parse[2])
                        shared_data.game.send_color = parse[2]
                        shared_data.game.color = "white" if parse[2] == "black" else "black"
                        print(shared_data.game.send_color)

    thread1 = threading.Thread(target=run_start)
    thread2 = threading.Thread(target=connection)
    thread1.start()
    thread2.start()