import socket

HOST = '0.0.0.0'
PORT = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server berjalan di port", PORT)
conn, addr = server.accept()
print("Client terhubung:", addr)

conn.sendall(b"Hello from server")  # server kirim pesan

conn.close()
server.close()
