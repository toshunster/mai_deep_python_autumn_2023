#! /usr/bin/env python3

import time
import socket
import multiprocessing as mp


def client(data):
    print(f"Client process")
    time.sleep(1)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 31000))
    sock.send(data)
    sock.close()
    print(f"response is {sock.recv(1024)}")

def server():
    print(f"Server process")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 31000))
    sock.listen(5)

    #while True:
    client_sock, addr = sock.accept()
    print(f"server: {addr=}")
    data = client_sock.recv(1024)
    client_sock.sendall(data.lower())

def main():
    server_pr = mp.Process(target=server)
    client_pr = mp.Process(target=client, args=("КОМУ НА РУСИ ЖИТЬ ХОРОШО".encode(),))

    server_pr.start()
    client_pr.start()

    server_pr.join()
    client_pr.join()

if __name__ == "__main__":
    main()
