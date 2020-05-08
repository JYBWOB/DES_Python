from MainWindow.ServerWindow import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtNetwork import QTcpServer, QHostAddress
from PyQt5.QtCore import *
from DES.DesOperate import DesOperate
from RSA.RSA import *
import sys


class Server(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.socket = QTcpServer()
        self.des = DesOperate()
        self.key = self.ui.key.text()
        self.client = []


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
        index = 0
        for index in range(len(self.client)):
            rxData = str(self.client[index].readAll(), 'utf-8')
            if rxData != "":
                self.ui.log.append("收到第%d个客户端消息" % index)
                self.ui.log.append("密文：%s" % rxData)
                solvedata = self.des.decry(rxData, self.key)
                self.ui.log.append("原文：%s" % solvedata)

    def sendMessage(self):
        string = self.ui.sendMessage.toPlainText()
        clientid = int(self.ui.clientid.text())
        if len(self.client) <= clientid:
            QMessageBox.information(self, "提示", "用户%d未建立连接" % clientid)
            return
        self.ui.log.append("发送原文：%s" % string)
        string = self.des.encry(string, self.key)
        self.ui.log.append("加密密文：%s" % string)
        self.client[clientid].write(string.encode())
        self.ui.sendMessage.setPlainText("")

    def newconnect(self):
        self.client.append(self.socket.nextPendingConnection())
        self.ui.log.append("连接成功")
        self.client[-1].readyRead.connect(self.on_socket_receive)
        self.client[-1].disconnected.connect(self.on_socket_disconnected)
        
    def on_socket_disconnected(self):
        self.ui.log.append("连接断开！")

