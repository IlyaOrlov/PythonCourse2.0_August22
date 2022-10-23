import socket


def decoder(text):
    dec_keys = {'$': 'i', '^': 'n', '*': 'm', '+': 'o', '@': 'h', ':': 'u', '%': 'a',
                '(': 'd', '#': 'l', '-': ' ', '№': 'r', ')': 'b', '!': 'e', ';': 'f', "decod": ""}
    for i in dec_keys.items():
        text = text.replace(i[0], i[1])
    return text


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    host = '127.0.0.1'
    port = 55345
    s.bind((host, port))
    s.listen(5)
    while True:
        con, adr = s.accept()
        with con:
            message = con.recv(1024).decode()
            print("connect")
            if "decod" in message:
                reply = decoder(message)
                con.send(reply.encode())
            else:
                print(message)
        print("disconnect")





