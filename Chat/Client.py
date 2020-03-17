from PyQt5.QtNetwork import QTcpSocket
from DES.DesOperate import DesOperate

class Client:
    def __init__(self):
        self.des = DesOperate()
        self.socket = QTcpSocket()

    def SetKey(self, keytext):
        self.key = keytext

    def Connect(self, host, port):
        self.socket.connect((host, port))

    def Send(self, message):
        ciphertext = self.des.encry(message, self.key)
        self.socket.send(ciphertext.encode())