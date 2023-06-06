import socket
import sys


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket succesfully created')

except socket.error as err:
    print(f'Socket creation failed with error {err}')    


port = 80

try:
    host_ip = socket.gethostbyname("github.com")

except socket.gaierror:
    print('Error resolving host')
    sys.exit()  


s.connect((host_ip, port))    
print(f'Socket connected succesfully to Github on port == {host_ip}')  