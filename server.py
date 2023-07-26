import socket
import threading


PORT=5050
HEAD=64
FORMAT='utf-8'

IP=socket.gethostbyname(socket.gethostname())
ADDR=(IP, PORT)

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

DISCONNECT_MSG="dc"

def handle_client(conn, addr):
    print(f"[New Connection] from : {addr}")
    connection_active=True

    while connection_active:
        try:
            msg_length=conn.recv(HEAD).decode(FORMAT)
            if msg_length:
                msg_length=int(msg_length)
                message = conn.recv(msg_length).decode(FORMAT)
                if message==DISCONNECT_MSG:
                    connection_active=False

                print(f"[{addr}] {message}")
                conn.send("seen".encode(FORMAT))
        except KeyboardInterrupt:
            connection_active=False
            break
    conn.close()


def start():
    server.listen()
    print(f"[Listening] Server {IP}")
    while True:
        conn, addr=server.accept()

        thread=threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[Active Connections] : {threading.active_count()-1}")


print("[Starting] The server is starting...")
start()