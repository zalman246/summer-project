#server

import socket
import select



MAX_MSG_LENGTH = 1024
SERVER_PORT = 5555
SERVER_IP = '0.0.0.0'

def print_client_sockets(client_sockets):
    for c in client_sockets:
        print("\t", c.getpeername())

print("Setting up server...")
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen()
print("Listening for clients...")
client_sockets = []
messages_to_send = []


while True:
    rlist, wlist, xlist = select.select([server_socket] + client_sockets, client_sockets, [])
    for current_socket in rlist:
#-----------------------------------------------------------------------------------
        if current_socket is server_socket: #new client
            connection, client_address = current_socket.accept()
            print("New client joined!", client_address)
            client_sockets.append(connection)
            print_client_sockets(client_sockets)
#-----------------------------------------------------------------------------------
        else: #old client
            data = current_socket.recv(MAX_MSG_LENGTH).decode()
            messages_to_send.append((current_socket, data))
            for msg in messages_to_send:
                current_socket, data = msg
                for socket in wlist:
                    if socket is not current_socket:        
                        socket.send(data.encode())
                        messages_to_send.remove(msg)