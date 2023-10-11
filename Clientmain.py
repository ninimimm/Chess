import socket
import subprocess
import threading

coordinate = None
game = None
if __name__ == "__main__":
    def run_start():
        subprocess.run(["python", "Clientstart.py"])
    thread1 = threading.Thread(target=run_start())
    thread1.start()
    def connection():
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('178.154.244.233', 8080))
        while True:
            if coordinate is None or coordinate[0] < 0 or coordinate[1] < 0 or coordinate[0] > 7 or coordinate[1] > 7:
                return
            message = f"{coordinate[0]} {coordinate[1]}"
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
            game.get_content(cages, figures, parse[2])
            coordinate = None
    thread2 = threading.Thread(target=connection())
    thread2.start()
