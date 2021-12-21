import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket()
        # self.server = "192.168.1.69"
        # self.port = 8080
        self.server = "2.tcp.ngrok.io"
        self.port = 14954
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def get_p(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except Exception as exception:
            print(exception)
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048*2))
        except socket.error as e:
            print(e)

