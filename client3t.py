import socket

HOST = "127.0.0.1"
PORT = 5050

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# timeout saat connect
client.settimeout(3)

try:
    client.connect((HOST, PORT))
    print("Terhubung ke server")

    # timeout saat membaca data
    client.settimeout(2)

    try:
        data = client.recv(1024)
        print("Data diterima:", data.decode())
    except socket.timeout:
        print("Koneksi timeout!")   # timeout saat read

except socket.timeout:
    print("Koneksi timeout!")       # timeout saat connect

client.close()
