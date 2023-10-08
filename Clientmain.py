import socket
import subprocess

if __name__ == "__main__":
    subprocess.run(["python", "Clientstart.py"])

def connection(coordinate, game, cl):
    if cl is None:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cl = client
        host = '127.0.0.1'
        port = 8080
        client.connect((host, port))
    message = f"{coordinate[0]} {coordinate[1]}"
    print("Отправляю сообщение на сервер")
    cl.send(message.encode('utf-8'))
    print("Отправил сообщение на сервер")

    print("Пытаюсь получить данные с сервера")
    data = cl.recv(1024).decode('utf-8')
    print("Получил данные с сервера")
    parse = data.split(",")
    game.cages = [x for x in parse[0].split()]
    game.figures = [x for x in parse[1].split()]

