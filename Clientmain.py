import socket
import subprocess

if __name__ == "__main__":
    subprocess.run(["python", "Clientstart.py"])

def connection(coordinate, game, cl):
    if cl is None:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cl = client
        client.connect(('127.0.0.1', 8080))
    if coordinate[0] < 0 or coordinate[1] < 0 or coordinate[0] > 7 or coordinate[1] > 7:
        return
    message = f"{coordinate[0]} {coordinate[1]}"
    print("Отправляю сообщение на сервер")
    cl.sendall(message.encode('utf-8'))
    print(message, "jnghfdbk [etne")
    print("Отправил сообщение на сервер")

    print("Пытаюсь получить данные с сервера")
    data = cl.recv(1024).decode('utf-8')
    print("Получил данные с сервера")
    parse = data.split(" ,")
    print(data)
    cages = [x for x in parse[0].split()]
    print(cages)
    figures = [x for x in parse[1].split()]
    print(figures)
    print(parse[2], "color")
    game.get_content(cages, figures, parse[2])
