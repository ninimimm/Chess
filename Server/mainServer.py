import socket
import random
import threading
import subprocess
from Game import Game

def handle_client(client, game, address):
    while True:
        try:
            data = client.recv(1024).decode('utf-8')
            if len(data) > 0:
                if data == "Легкий" or data == "Сложный":
                    if data == "Легкий":
                        def run():
                            subprocess.call(["/usr/bin/python3", "/home/chesseditor/Chess/EasyBot/EasyBotmain.py"])
                        script1_thread = threading.Thread(target=run)
                        script1_thread.start()
                    else:
                        def run():
                            subprocess.call(["/usr/bin/python3", "/home/chesseditor/Chess/HardBot/Botmain.py"])
                        script1_thread = threading.Thread(target=run)
                        script1_thread.start()
                elif "possible moves" in data:
                    if game.players_ip[address[0]][1]:
                        split = data.split(",")
                        response = game.get_possible_moves(data.split(',')[1].split(), split[2])
                        send = "possible moves" + ",".join([f"{key[0]} {key[1]}:{'|'.join(value)}" for key, value in response.items()])
                        client.sendall(send.encode('utf-8'))
                elif any(x in data for x in ["Queen", "Horse", "Elephant", "Rook"]):
                    game.ready = True
                    massage = data.split(",")
                    cord = massage[1].split()
                    game.create_figure(massage[0], (int(cord[0]), int(cord[1])), address[0])
                    for value in game.players_ip.values():
                        value[1] = not (value[1])
                    for cl in clients:
                        cl.sendall(game.get_response(address[0]).encode('utf-8'))
                else:
                    message = data.split()
                    print("Пытаюсь отправить данные клиенту")
                    flag = game.dict_cages[(int(message[0]), int(message[1]))].color == "green"
                    response = game.on_click((int(message[0]), int(message[1])), address[0])
                    if len(clients) > 1 and game.players_ip[address[0]][1]:
                        client.sendall(response.encode('utf-8'))
                        if flag and "choice" not in response:
                            for value in game.players_ip.values():
                                value[1] = not (value[1])
                            for cl in clients:
                                if client != cl:
                                    if "победа" in response:
                                        response = f"{response[:-6]}поражение"
                                    if game.players_ip[address[0]][0] == "white":
                                        cl.sendall("black".join((response.rsplit("white", 1))).encode('utf-8'))
                                    else:
                                        cl.sendall("white".join((response.rsplit("black", 1))).encode('utf-8'))
                    print("Отправил данные клиенту")
        except (ConnectionResetError, OSError) as Ex:
            print(Ex)
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
    colors = ["white", "black"]
    rand = random.randint(0, 1)
    ip_save = None

    while True:
        client, address = server.accept()
        if len(clients) == 1:
            game.players_ip[ip_save] = ["white", True]
            game.players_ip[address[0]] = ["black", False]
            data = [f"{game.dict_cages[(j, i)].figure.color}_{game.dict_cages[(j, i)].figure.name}{game.dict_cages[(j, i)].figure.index}"
                    if game.dict_cages[(j, i)].figure is not None else "None" for i in range(8) for j in range(8)]

            response = game.get_possible_moves(data, "white")
            send = "possible moves" + ",".join(
                [f"{key[0]} {key[1]}:{'|'.join(value)}" for key, value in response.items()]) + "<>white 0"
            clients[0].sendall(send.encode('utf-8'))

            response = game.get_possible_moves(data, "black")
            send = "possible moves" + ",".join(
                [f"{key[0]} {key[1]}:{'|'.join(value)}" for key, value in response.items()]) + "<>black 1"
            client.sendall(send.encode('utf-8'))
            print(game.players_ip)
        ip_save = address[0]
        clients.append(client)
        print(f"Подключен клиент {address}")
        client_handler = threading.Thread(target=handle_client, args=(client, game, address))
        client_handler.start()
