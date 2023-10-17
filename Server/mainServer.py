import socket
import threading
from Game import Game

def handle_client(client, game, address):
    while True:
        try:
            data = client.recv(1024).decode('utf-8')
            if len(data) > 0:
                if "possible moves" in data:
                    split = data.split(",")
                    response = game.get_possible_moves(data.split(',')[1].split(), split[2])
                    print(response)
                    client.recv("possible moves" + ",".join([f"{key}:{' '.join(value)}"for key, value in response]))
                elif any(x in data for x in ["Queen", "Horse", "Elephant", "Rook"]):
                    game.ready = True
                    massage = data.split(",")
                    cord = massage[1].split()
                    game.create_figure(massage[0], (int(cord[0]), int(cord[1])), address[0])
                    print(game.players_ip)
                    for value in game.players_ip.values():
                        value[1] = not (value[1])
                    print(game.players_ip)
                    for cl in clients:
                        cl.sendall(game.get_response(address[0]).encode('utf-8'))
                else:
                    print(data)
                    message = data.split()
                    print(message)
                    print("Пытаюсь отправить данные клиенту")
                    flag = game.dict_cages[(int(message[0]), int(message[1]))].color == "green"
                    response = game.on_click((int(message[0]), int(message[1])), address[0])
                    if game.players_ip[address[0]][1]:
                        client.sendall(response.encode('utf-8'))
                        if flag and "choice" not in response:
                            for value in game.players_ip.values():
                                value[1] = not (value[1])
                            for cl in clients:
                                if client != cl:
                                    cl.sendall(response.encode('utf-8'))
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


    while True:
        client, address = server.accept()
        clients.append(client)
        print(f"Подключен клиент {address}")
        client_handler = threading.Thread(target=handle_client, args=(client, game, address))
        client_handler.start()
