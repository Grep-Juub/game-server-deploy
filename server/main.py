import multiprocessing
import time
import socket

LISTEN_ADDRESS = "127.0.0.1"
LISTEN_PORT = 7778
SERVER_TIMEOUT = 600
BUFFER_SIZE = 1024

def server(addr, port):
    """
        A simple socket listener that print all it recieve to the standart ouptut
    """
    serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSock.bind((addr, port))

    print(f'[{LISTEN_ADDRESS}:{LISTEN_PORT}] Server is running... timeout in {SERVER_TIMEOUT}s')
    while True:
        data, addr = serverSock.recvfrom(BUFFER_SIZE)
        print(f'[{LISTEN_ADDRESS}:{LISTEN_PORT}] <= [{addr[0]}:{addr[1]}] {data.decode("utf-8")}')

if __name__ == '__main__':
    p = multiprocessing.Process(target=server, name="Server", args=(LISTEN_ADDRESS, LISTEN_PORT))
    p.start()

    time.sleep(SERVER_TIMEOUT)

    p.terminate()
    p.join()
