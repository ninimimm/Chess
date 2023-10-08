import socket
import threading
from Game import Game

def handle_client(client, game):
    while True:
        try:
            data = client.recv(1024).decode('utf-8')
            if not data:
                break  # Клиент отключился, завершаем обработку
            message = data.split()
            print(message)
            if len(message) > 0:
                print("Пытаюсь отправить данные клиенту")
                print(message)
                response = game.on_click((int(message[0]), int(message[1]))).encode('utf-8')
                client.send(response)
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
    server.bind(('127.0.0.1', 8080))
    server.listen(2)
    print("Сервер запущен и ждет подключений.")

    while True:
        client, address = server.accept()
        print(f"Подключен клиент {address}")
        client_handler = threading.Thread(target=handle_client, args=(client, game))
        client_handler.start()