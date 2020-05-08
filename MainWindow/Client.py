from MainWindow.ClientWindow import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtNetwork import QTcpSocket
from PyQt5.QtCore import *
from DES.DesOperate import DesOperate
import sys


class Client(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.socket = QTcpSocket()
        self.des = DesOperate()
        self.key = self.ui.key.text()

        self.ui.connect.clicked.connect(self.Connect)
        self.ui.send.clicked.connect(self.sendMessage)
        self.ui.setKey.clicked.connect(self.setKey)
        self.show()

    def setKey(self):
        self.key = self.ui.key.text()
        self.ui.log.append("设置密钥为：%s" % self.key)
        QMessageBox.information(self, "提示", "设置成功")

    def Connect(self):
        self.serverhost = self.ui.host.text()
        self.serverport = int(self.ui.port.text())
        self.socket.connectToHost(self.serverhost, self.serverport)
        self.socket.connected.connect(self.on_socket_connected)
        self.socket.disconnected.connect(self.on_socket_disconnected)
        self.socket.readyRead.connect(self.on_socket_receive)

    def on_socket_receive(self):
        rxData = str(self.socket.readAll(), 'utf-8')
        self.ui.log.append("收到密文：%s" % rxData)
        solvedata = self.des.decry(rxData, self.key)
        self.ui.log.append("解密原文：%s" % solvedata)

    def sendMessage(self):
        string = self.ui.sendMessage.toPlainText()
        self.ui.log.append("发送原文：%s" % string)
        string = self.des.encry(string, self.key)
        self.ui.log.append("加密密文：%s" % string)
        self.socket.write(string.encode())
        self.ui.sendMessage.setPlainText("")

    def on_socket_connected(self):
        self.ui.log.append("已连接到%s:%d" % (self.serverhost, self.serverport))

    def on_socket_disconnected(self):
        self.ui.log.append("连接断开！")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    client = Client()
    sys.exit(app.exec_())

