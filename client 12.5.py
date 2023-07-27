#client

import socket
import select
import threading


client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 5555))

def job():
    while True:
        print('\n')
        msg = input('enter message:')
        client_socket.send((msg).encode())
        if msg == "quit": 
            break

t = threading.Thread(target=job)
t.start()

while True:
    try:
        datat=client_socket.recv(1024).decode()
        if datat != '':
            print('\n')
            print(datat)
            print('\n')
            print('enter message:')
    except:
        pass
