import socket
import threading
from Game import Game

def handle_client(client, game, address):
    while True:
        try:
            data = client.recv(1024).decode('utf-8')
            if len(data) > 0:
                message = data.split()
                print(message)
                print("Пытаюсь отправить данные клиенту")
                response = game.on_click((int(message[0]), int(message[1])), address[0]).encode('utf-8')
                for cl in clients:
                    cl.send(response)
                print("Отправил данные клиенту")
        except (ConnectionResetError, OSError):
            print("Клиент отключился")
            break
    client.close()

if __name__ == '__main__':
    square_size = 90
    diffy = 80
    diffx = 140
    game = Game(square_size, diffy, diffx)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 8080))
    server.listen()
    print("Сервер запущен и ждет подключений.")
    clients = []

    try:
        while True:
            client, address = server.accept()
            clients.append(client)
            print(f"Подключен клиент {address}")
            client_handler = threading.Thread(target=handle_client, args=(client, game, address))
            client_handler.start()
    finally:
        server.close()
