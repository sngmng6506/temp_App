import socket


def RequestFromClient(SERVER_IP,SENDING_URL):
    SERVER_PORT = 1097
    SERVER_ADDR = (SERVER_IP, SERVER_PORT)
    MAX_SIZE = 1024

    #client socket
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client_socket:
        client_socket.connect(SERVER_ADDR)
        client_socket.send(SENDING_URL.encode())
        msg = client_socket.recv(MAX_SIZE)
        print("resp from server : {}".format(msg))


#SERVER_IP = '172.30.1.11'
#SENDING_URL = ('https://www.youtube.com/watch?v=3lTUF2IbMR4')
#RequestFromClient(SERVER_IP,SENDING_URL)

