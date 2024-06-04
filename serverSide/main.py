#region imports
import logging
import socket
import threading
import log_config
#endregion

#region declarations
SERVER_IP = 'localhost'
SERVER_PORT = 12345
done = False
#endregion

#region functions
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen()
    print('Waiting for a connection')
    return server_socket
def client_traffic(client_socket, addr):
        print(f'Got a connection from {addr}')
        try:
            client_alias = client_socket.recv(1024).decode('utf-8')
            if client_alias != "":
                client_socket.send(f"You have succesfully connected to {SERVER_IP}:{SERVER_PORT} as {client_alias}".encode("utf-8"))
                print(f'User: {client_alias} connected')
                logging.debug(f'User: {client_alias} has connected')
            else:
                client_socket.close()
        except:
            logging.exception('There was an error while connecting')
            client_socket.close()
#endregion

if __name__ == '__main__':
    log_config.log(__file__)
    logging.debug(f"Starting server at {SERVER_IP}:{SERVER_PORT}")
    try:
        server_socket = start_server()
        logging.debug(f'Server started and listening on port {SERVER_PORT}')
        while not done:
            client_socket, addr = server_socket.accept()
            logging.debug(f'Accepted connection from {addr}')
            clients_handler = threading.Thread(target=client_traffic, args=(client_socket, addr))
            clients_handler.start()
    except:
        logging.exception('There was an error opening the server')

