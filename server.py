import socket
import threading


PORT=5050
HEAD=64
FORMAT='utf-8'


SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER, PORT)

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

DISCONNECT_MSG="![Disconnected]"

def handle_client(conn, addr):
    print(f"[New Connection] from : {addr}")
    connection_active=True

    while connection_active:
        msg_length=conn.recv(HEAD).decode(FORMAT)
        if msg_length:
            msg_length=int(msg_length)
            message = conn.recv(msg_length).decode(FORMAT)
            if message==DISCONNECT_MSG:
                connection_active=False

            print(f"[{addr}] {message}")
    conn.close()


def start():
    server.listen()
    print(f"[Listening] Server {SERVER}")
    while True:
        conn, addr=server.accept()

        thread=threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[Active Connections] : {threading.active_count()-1}")


print("[Starting] The server is starting...")
start()