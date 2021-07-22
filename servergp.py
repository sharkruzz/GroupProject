import socket
import threading

host = '192.168.56.105'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listening..")
print(" _____ _______ _______ _  _   _  _    ___    __  __                                          ")
print("|_   _|__   __|__   __| || | | || |  / _ \  |  \/  |                                         ")
print("  | |    | |     | |  | || |_| || |_| | | | | \  / | ___  ___ ___  ___ _ __   __ _  ___ _ __ ")
print("  | |    | |     | |  |__   _|__   _| | | | | |\/| |/ _ \/ __/ __|/ _ \ '_ \ / _` |/ _ \ '__|")
print(" _| |_   | |     | |     | |    | | | |_| | | |  | |  __/\__ \__ \  __/ | | | (_| |  __/ |   ")
print("|_____|  |_|     |_|     |_|    |_|  \___/  |_|  |_|\___||___/___/\___|_| |_|\__, |\___|_|   ")
print("                                                                              __/ |          ")
print("                                                                             |___/           ")
receive()
