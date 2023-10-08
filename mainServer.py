from Game import Game
import socket
if __name__ == '__main__':

    square_size = 90
    diffy = 80
    diffx = 140

    game = Game(square_size, diffy, diffx)
    server = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    server.recvfrom(8080)
    server.bind(('127.0.0.1', 8080))
    server.listen(2)

    client, address = server.accept()

    while True:
        print("Читаю данные клиента")
        data = client.recv(1024)
        print("Прочитал данные клиента")
        print(str(data))

        message = data.decode().split()

        if not message:
            break

        print("Пытаюсь отправить данные клиенту")
        response = game.on_click((int(message[0]), int(message[1]))).encode('utf-8')
        client.send(response)
        print("Отправил данные клиенту")
