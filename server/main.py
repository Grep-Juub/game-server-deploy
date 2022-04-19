"""
author: Paul Fournet
desc: Run a simple udp server
"""

import os
import multiprocessing
import time
import socket

LISTEN_ADDRESS = os.getenv("LISTEN_ADDRESS", "127.0.0.1")
LISTEN_PORT = int(os.getenv("LISTEN_PORT", "7778"))
SERVER_TIMEOUT = int(os.getenv("SERVER_TIMEOUT", "600"))
BUFFER_SIZE = int(os.getenv("BUFFER_SIZE", "1024"))


def server(addr, port):
    """
    A simple socket listener that print all it recieve to the standart ouptut
    """
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_sock.bind((addr, port))

    print(
        f"[{LISTEN_ADDRESS}:{LISTEN_PORT}] Server is running... timeout in {SERVER_TIMEOUT}s"
    )
    while True:
        data, addr = server_sock.recvfrom(BUFFER_SIZE)
        print(
            f'[{LISTEN_ADDRESS}:{LISTEN_PORT}] <= [{addr[0]}:{addr[1]}] {data.decode("utf-8")}'
        )


if __name__ == "__main__":
    PROCESS = multiprocessing.Process(
        target=server, name="Server", args=(LISTEN_ADDRESS, LISTEN_PORT)
    )
    PROCESS.start()

    time.sleep(SERVER_TIMEOUT)

    PROCESS.terminate()
    PROCESS.join()
