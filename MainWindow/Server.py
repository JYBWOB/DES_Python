from MainWindow.ServerWindow import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtNetwork import QTcpServer, QHostAddress
from PyQt5.QtCore import *
from DES.DesOperate import DesOperate
import sys


class Server(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.socket = QTcpServer()
        self.des = DesOperate()
        self.key = self.ui.key.text()

        self.ui.bind.clicked.connect(self.bind)
        self.ui.send.clicked.connect(self.sendMessage)
        self.ui.setKey.clicked.connect(self.setKey)
        
        self.show()

    def setKey(self):
        self.key = self.ui.key.text()
        self.ui.log.append("设置密钥为：%s" % self.key)
        QMessageBox.information(self, "提示", "设置成功")

    def bind(self):
        self.bindport = int(self.ui.port.text())
        self.socket.listen(QHostAddress.LocalHost,self.bindport)
        self.socket.newConnection.connect(self.newconnect)
        self.ui.log.append("正在监听端口 %d" % self.bindport)

    def on_socket_receive(self):
        rxData = str(self.client.readAll(), 'utf-8')
        self.ui.log.append("收到密文：%s" % rxData)
        solvedata = self.des.decry(rxData, self.key)
        self.ui.log.append("解密原文：%s" % solvedata)

    def sendMessage(self):
        string = self.ui.sendMessage.toPlainText()
        self.ui.log.append("发送原文：%s" % string)
        string = self.des.encry(string, self.key)
        self.ui.log.append("加密密文：%s" % string)
        self.client.write(string.encode())
        self.ui.sendMessage.setPlainText("")

    def newconnect(self):
        self.client = self.socket.nextPendingConnection()
        self.ui.log.append("连接成功")
        self.client.readyRead.connect(self.on_socket_receive)
        self.client.disconnected.connect(self.on_socket_disconnected)
        
    def on_socket_disconnected(self):
        self.ui.log.append("连接断开！")

