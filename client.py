import socket


HEADER=64
PORT=5050
FORMAT='utf-8'
DISCONNECT_MSG="![Disconnected]"
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,PORT)

print(f"SERVER : {SERVER}\n")

def send(msg):
    send_message=msg.encode(FORMAT)
    msg_length=len(send_message)
    send_size=str(msg_length).encode(FORMAT)
    send_size+=b' '*(HEADER-len(send_size))

    client.send(send_size)
    client.send(send_message)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

loop = True
while loop:
    user_input=input("Enter the message: ")
    if user_input=='':
        break
    try:
        send(user_input)
    except ConnectionAbortedError:
        print("[Disconnected] client disconnect request")
        break
        



