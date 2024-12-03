from PyQt6.QtWidgets import QPushButton,  QMainWindow
class InitYellow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pushButton = QPushButton(self)
        self.setGeometry(300, 300, 300, 300)
        self.yeee = False
        self.pushButton = QPushButton(self)
        self.pushButton.setText('НЕ ТОЛЬКО ЖЕЛТЫЙ!')
        self.pushButton.resize(200, 50)
        self.pushButton.clicked.connect(self.yellow)
