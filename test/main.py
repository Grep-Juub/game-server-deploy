import socket
import sys

byte_message = bytes(sys.argv[3], "utf-8")
opened_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
opened_socket.sendto(byte_message, (sys.argv[1], int(sys.argv[2])))
