import socket
import select
import threading
from ClientGui import ClientGui
from ClientGame import ClientGame
class SharedData:
    def __init__(self):
        self.coordinate = None
        self.game = None
        self.answer_button = None

# Создаем единственный экземпляр SharedData
shared_data = SharedData()
gui = None

# В ваших потоках используйте shared_data.coordinate и shared_data.gam
if __name__ == "__main__":
    def run_start():
        global gui
        gui = ClientGui(shared_data)
        gui.root.mainloop()
    def connection():
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('178.154.244.233', 8080))
        while True:
            if shared_data.coordinate is not None:
                if shared_data.coordinate[0] < 0 or shared_data.coordinate[1] < 0 or shared_data.coordinate[0] > 7 or shared_data.coordinate[1] > 7:
                    shared_data.coordinate = None
                    continue
                message = f"{shared_data.coordinate[0]} {shared_data.coordinate[1]}"
                client.sendall(message.encode('utf-8'))
                shared_data.coordinate = None

            ready = select.select([client], [], [], 0.05)
            if ready[0]:
                data = client.recv(1024).decode('utf-8')
                if len(data) > 0:
                    if data.split()[0] == "choice":
                        gui.game.choose_figure(data.split()[1])
                        while shared_data.answer_button is None:
                            continue
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
                        shared_data.game.get_content(cages, figures, parse[2])

    thread1 = threading.Thread(target=run_start)
    thread2 = threading.Thread(target=connection)
    thread1.start()
    thread2.start()