import socket


host = '127.0.0.1'
port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
client.send('qazesxedcr'.encode())
print(f'Получено: "{client.recv(1024).decode()}"')

client.close()