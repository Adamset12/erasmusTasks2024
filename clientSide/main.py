# Server Script (server.py)
import socket
import logging
import log_config
HOST = 'localhost'
PORT = 12345
def connect_to_server(HOST, PORT):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((HOST, PORT))
        user_alias = input("What's your name?: ")
        client_socket.send(f"{user_alias}".encode("utf-8"))
        logging.info(f'Connection established as {user_alias}')
        message = client_socket.recv(1024).decode("utf-8")
        print(message)
        client_socket.close()
        logging.info(f"{user_alias} has ended its connection.")
    except:
        print("Couldn't connect to the server")


if __name__ == "__main__":
    log_config.log(__file__)
    connect_to_server(HOST, PORT)