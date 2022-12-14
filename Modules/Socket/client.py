import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECTED_MESSAGE = 'disconnected!'
SERVER = '192.168.159.1'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_length = str(msg_len).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

send("Client Connected To Server!")
send(DISCONNECTED_MESSAGE)
    