import socket
import threading

# about to dynamically try to implement socket programming on one server from multiple clients.

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) #dynamically obtains the ip address of the machine server is setup on
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def Client_end(conn, addr):
    print(f"[CONNECTED] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            print(f"[{addr}] {msg}")
            if msg == DISCONNECT_MESSAGE:
                connected = False
        
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True: 
        conn, addr = server.accept()
        thread = threading.Thread(target=Client_end, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
print("[STARTING] server is starting...")
start()



    


