import socket
import select
import threading
from BotGame import BotGame
class SharedData:
    def __init__(self):
        self.coordinate = None
        self.game = None
        self.answer_button = None
        self.copy_field = None
        self.can_use = False
        self.game_dict = {}

# Создаем единственный экземпляр SharedData
shared_data = SharedData()
gui = None

# В ваших потоках используйте shared_data.coordinate и shared_data.gam
if __name__ == "__main__":  # pragma: no cover
    def run_start():
        global gui
        shared_data.game = BotGame(shared_data)

    def wait_result(client):
        #print("вызвали!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        incoming, outcoming = shared_data.game.get_content(shared_data.game_dict, shared_data.game.send_color)
        client.sendall(f"{incoming[0]} {incoming[1]}".encode('utf-8'))
        client.recv(1024).decode('utf-8')
        client.sendall(f"{outcoming[0]} {outcoming[1]}".encode('utf-8'))
        client.recv(1024).decode('utf-8')

    def connection():
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('178.154.244.233', 8080))
        client.sendall("0 7".encode('utf-8'))
        while True:
            if shared_data.game.send_color is not None:
               #print(shared_data.copy_field)
               client.sendall(f"possible moves,{' '.join([x[j] for j in range(8) for x in shared_data.copy_field])},{shared_data.game.send_color}".encode('utf-8'))
               shared_data.game.send_color = None
            ready = select.select([client], [], [], 0.05)
            if ready[0]:
                data = client.recv(1024).decode('utf-8')
                if len(data) > 0:
                    if "possible moves" in data:
                        info = data
                        ind = None
                        if "<>" in data:
                            info = data.split('<>')
                            col, ind = info[1].split()
                            shared_data.game.color = col
                            #print(info[1])
                            info = info[0]
                            #print(info)
                        #print(info)
                        parse = info[14:].split(",")
                        if parse != ['']:
                            shared_data.game_dict = {}
                            for item in parse:
                                item_parse = item.split(":")
                                key = [int(x) for x in item_parse[0].split()]
                                shared_data.game_dict[(key[0], key[1])] = [(int(x.split()[0]), int(x.split()[1])) for x in item_parse[1].split('|')]
                            shared_data.can_use = True
                            if not shared_data.game.is_running and ("<>" in data and ind == "0" or "<>" not in data):
                                shared_data.can_use = False
                                thread4 = threading.Thread(target=wait_result, args=(client,))
                                thread4.start()
                        
                    elif data.split()[0] == "choice":
                        gui.game.choose_figure(data.split()[1])
                        while shared_data.answer_button is None:
                            continue
                        client.sendall(shared_data.answer_button.encode('utf-8'))
                        shared_data.answer_button = None
                    else:
                        if len(parse) > 0:
                            parse = data.split(" ,")
                            figures = [x for x in parse[1].split()]
                            for i in range(8):
                                for j in range(8):
                                    shared_data.game.string_images[j][i] = figures[i * 8 + j]
                                    shared_data.copy_field[j][i] = figures[i * 8 + j]
                            shared_data.game.send_color = shared_data.game.color

    thread1 = threading.Thread(target=run_start)
    thread2 = threading.Thread(target=connection)
    thread1.start()
    thread2.start()