from PyQt6.QtWidgets import QPushButton, QWidget
def main():
    class YellowDots(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            self.setGeometry(300, 300, 300, 300)
            self.setWindowTitle('желтые точки')



if __name__ == '__main__':
    main()