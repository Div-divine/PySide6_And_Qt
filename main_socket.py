import socket

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket succesfully created')

port = 12345
s.bind(('', port))
print('Socket binded to port', port)

s.listen(5)
print('Socket Listening')

while True:
    
    c, addr = s.accept()
    print(f'Socket connecting to {addr}')

    message = ('Thank you for connecting')
    c.send(message.encode())

    c.close()