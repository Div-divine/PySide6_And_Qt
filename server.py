import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 50540

server.bind((host, port))
server.listen()

clients = []
aliases = []

def broadcast(message):

    for client in clients:
        client.send(message)

def client_connect(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)

        except:
            index = clients.index(client)    
            clients.remove(client)
            client.close()
