import socket

HOST = '0.0.0.0'
PORT = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server berjalan di port", PORT)

conn, addr = server.accept()
print("Client terhubung:", addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    print("Dari client:", data.decode())  # tampil di server

    conn.sendall(data)  # echo kembali

conn.close()
