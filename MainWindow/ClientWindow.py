# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ClientWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 544)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sendMessage = QtWidgets.QTextEdit(self.centralwidget)
        self.sendMessage.setGeometry(QtCore.QRect(30, 390, 511, 121))
        self.sendMessage.setObjectName("sendMessage")
        self.send = QtWidgets.QPushButton(self.centralwidget)
        self.send.setGeometry(QtCore.QRect(550, 430, 81, 41))
        self.send.setObjectName("send")
        self.log = QtWidgets.QTextEdit(self.centralwidget)
        self.log.setGeometry(QtCore.QRect(30, 110, 611, 271))
        self.log.setObjectName("log")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 601, 37))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.host = QtWidgets.QLineEdit(self.layoutWidget)
        self.host.setObjectName("host")
        self.horizontalLayout.addWidget(self.host)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.port = QtWidgets.QLineEdit(self.layoutWidget)
        self.port.setObjectName("port")
        self.horizontalLayout.addWidget(self.port)
        self.connect = QtWidgets.QPushButton(self.layoutWidget)
        self.connect.setObjectName("connect")
        self.horizontalLayout.addWidget(self.connect)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(31, 70, 321, 37))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.key = QtWidgets.QLineEdit(self.widget)
        self.key.setObjectName("key")
        self.horizontalLayout_2.addWidget(self.key)
        self.setKey = QtWidgets.QPushButton(self.widget)
        self.setKey.setObjectName("setKey")
        self.horizontalLayout_2.addWidget(self.setKey)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Client"))
        self.send.setText(_translate("MainWindow", "发送"))
        self.label.setText(_translate("MainWindow", "服务端IP:"))
        self.host.setText(_translate("MainWindow", "127.0.0.1"))
        self.label_2.setText(_translate("MainWindow", "服务端Port:"))
        self.port.setText(_translate("MainWindow", "8888"))
        self.connect.setText(_translate("MainWindow", "连接"))
        self.label_3.setText(_translate("MainWindow", "密钥："))
        self.key.setText(_translate("MainWindow", "abcdefgh"))
        self.setKey.setText(_translate("MainWindow", "确定"))

