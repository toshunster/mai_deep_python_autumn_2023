import socket

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_sock.bind(("localhost", 15000))
server_sock.listen()

while True:
    client_sock, addr = server_sock.accept()
    print(f"Accepting {addr}")
    while True:
        data = client_sock.recv(4096)
        if not data:
            break
        client_sock.send(data.decode().upper().encode())
    client_sock.close()
