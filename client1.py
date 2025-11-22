import socket

HOST = '127.0.0.1'
PORT = 5050

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.sendall(b"Tes Koneksi")
data = client.recv(1024)

print("Balasan dari server:", data.decode())
client.close()
