# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ServerWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 502)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sendMessage = QtWidgets.QTextEdit(self.centralwidget)
        self.sendMessage.setGeometry(QtCore.QRect(20, 350, 531, 121))
        self.sendMessage.setObjectName("sendMessage")
        self.send = QtWidgets.QPushButton(self.centralwidget)
        self.send.setGeometry(QtCore.QRect(570, 390, 81, 41))
        self.send.setObjectName("send")
        self.log = QtWidgets.QTextEdit(self.centralwidget)
        self.log.setGeometry(QtCore.QRect(20, 70, 641, 271))
        self.log.setObjectName("log")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 299, 37))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.port = QtWidgets.QLineEdit(self.layoutWidget)
        self.port.setObjectName("port")
        self.horizontalLayout.addWidget(self.port)
        self.bind = QtWidgets.QPushButton(self.layoutWidget)
        self.bind.setObjectName("bind")
        self.horizontalLayout.addWidget(self.bind)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(340, 20, 321, 37))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.key = QtWidgets.QLineEdit(self.layoutWidget1)
        self.key.setObjectName("key")
        self.horizontalLayout_2.addWidget(self.key)
        self.setKey = QtWidgets.QPushButton(self.layoutWidget1)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Server"))
        self.send.setText(_translate("MainWindow", "发送"))
        self.label_2.setText(_translate("MainWindow", "监听端口:"))
        self.port.setText(_translate("MainWindow", "8888"))
        self.bind.setText(_translate("MainWindow", "监听"))
        self.label_3.setText(_translate("MainWindow", "密钥："))
        self.key.setText(_translate("MainWindow", "abcdefgh"))
        self.setKey.setText(_translate("MainWindow", "确定"))

