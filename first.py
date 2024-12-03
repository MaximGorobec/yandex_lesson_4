from PyQt6.QtWidgets import QPushButton, QWidget, QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor
from random import randint
from PyQt6 import uic
import sys


class YellowDots(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.yeee = False
        self.pushButton.clicked.connect(self.yellow)

    def yellow(self):
        self.yeee = True
        self.update()
    def paintEvent(self, event):
        if self.yeee:
            qp = QPainter()
            qp.begin(self)
            ran = randint(10, 100)
            ran_cor = (randint(10, 300), randint(10, 300))
            qp.setBrush(QColor(255, 255, 0))
            qp.drawEllipse(ran_cor[0], ran_cor[1], ran, ran)
            qp.end()
        self.yeee = False




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowDots()
    ex.show()
    sys.exit(app.exec())