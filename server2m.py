import socket
import threading

HOST = "0.0.0.0"
PORT = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []  # menyimpan daftar client

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            client.send(message)

def handle_client(conn, addr):
    print(f"Client terhubung: {addr}")
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            print(f"[{addr}] {data.decode()}")
            broadcast(data, conn)
        except:
            break
    
    clients.remove(conn)
    conn.close()
    print(f"Client keluar: {addr}")

print("Chat Server berjalan...")
while True:
    conn, addr = server.accept()
    clients.append(conn)
    threading.Thread(target=handle_client, args=(conn, addr)).start()
