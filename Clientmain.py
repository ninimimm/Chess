import socket
import subprocess
import threading
from ClientGui import ClientGui

class SharedData:
    def __init__(self):
        self.coordinate = None
        self.game = None

# Создаем единственный экземпляр SharedData
shared_data = SharedData()

# В ваших потоках используйте shared_data.coordinate и shared_data.gam
if __name__ == "__main__":
    def run_start():
        gui = ClientGui(shared_data)
        gui.root.mainloop()
    def connection():
        global shared_data
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('178.154.244.233', 8080))
        while True:
            print(shared_data.coordinate, shared_data.game)
            if shared_data.coordinate is not None:
                if shared_data.coordinate[0] < 0 or shared_data.coordinate[1] < 0 or shared_data.coordinate[0] > 7 or shared_data.coordinate[1] > 7:
                    print(shared_data.game)
                    continue
                message = f"{shared_data.coordinate[0]} {shared_data.coordinate[1]}"
                print("Отправляю сообщение на сервер")
                client.sendall(message.encode('utf-8'))
                print(message, "jnghfdbk [etne")
                print("Отправил сообщение на сервер")

            print("Пытаюсь получить данные с сервера")
            data = client.recv(1024).decode('utf-8')
            print("Получил данные с сервера")
            parse = data.split(" ,")
            print(data)
            cages = [x for x in parse[0].split()]
            print(cages)
            figures = [x for x in parse[1].split()]
            print(figures)
            print(parse[2], "color")
            shared_data.game.get_content(cages, figures, parse[2])
            shared_data.coordinate = None
    thread1 = threading.Thread(target=run_start)
    thread2 = threading.Thread(target=connection)
    thread1.start()
    thread2.start()
