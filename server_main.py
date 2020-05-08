from PyQt5.QtWidgets import *
from MainWindow.Client import Client
from MainWindow.Server import Server
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    server = Server()
    sys.exit(app.exec_())
