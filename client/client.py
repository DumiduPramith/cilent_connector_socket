import socket,select, sys, time
from connection import Connection

ADDR = (socket.gethostbyname(socket.gethostname()), 5051)
FORMAT = 'utf-8'
HEADER = 64

class HandleConnection():
    def __init__(self,connection):
        self.server = connection
    
    def run(self):
        global CONNECTION
        socket_list = [self.server.server]
        read_socket, write_socket, error = select.select(socket_list,[],socket_list,0.5)
        for socket in read_socket:
            if socket is self.server.server:
                msg = socket.recv(10).decode(FORMAT)
                if msg == '':
                    socket.close()
                    CONNECTION = False
                print(msg)
            
        # self.on_read()
        # print(write_socket)
    
    def on_read(self):
        msg = sys.stdin.readline()
        if msg:
            self.server.send(msg.encode(FORMAT))

conn = Connection()
input = HandleConnection(conn)

CONNECTION = True
while CONNECTION:
    input.run()
