from Game import Game
import socket
if __name__ == '__main__':
    square_size = 90
    diffy = 80
    diffx = 140
    game = Game(square_size, diffy, diffx)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 8080))
    server.listen(2)
    client, address = server.accept()
    while True:
        data = client.recv(1024).decode('utf-8')
        message = data.split()
        print(message)
        if len(message) > 0:
            print("Пытаюсь отправить данные клиенту")
            print(message)
            response = game.on_click((int(message[0]), int(message[1]))).encode('utf-8')
            client.send(response)
            print("Отправил данные клиенту")
